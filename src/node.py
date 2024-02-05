from itertools import chain
from queue import Queue
from random import randint
from socket import (
    AF_INET,
    IPPROTO_IP,
    IP_ADD_MEMBERSHIP,
    IP_MULTICAST_TTL,
    SHUT_RDWR,
    SOCK_DGRAM,
    SOCK_STREAM,
    SOL_SOCKET,
    SO_REUSEADDR,
    inet_aton,
    socket
)
from threading import Thread, Lock, Semaphore
from time import sleep
from typing import List

MULTICAST_ADDR = "224.0.0.10"
MULTICAST_PORT = 49152

ADVERTISE_SERV_DELAY = 3


def getMachineIp():
    """Get the IP address of the machine."""
    s = socket(AF_INET, SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(("10.254.254.254", 1))
        ip = s.getsockname()[0]
    except OSError:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


class NodeConnection:
    def __init__(self, localIp):
        self.localIp = localIp
        self.castSocket = socket(AF_INET, SOCK_DGRAM)
        self.notifications = Queue(10)
        self._configCastSocket()
        self.castListenThread: Thread = None
        self.startListen()

    def _configCastSocket(self):
        self.castSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.castSocket.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, 2)
        self.castSocket.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP,
                                   inet_aton(MULTICAST_ADDR) + inet_aton("0.0.0.0"))
        self.castSocket.bind(("0.0.0.0", MULTICAST_PORT))

    def cast(self, msg: str):
        self.castSocket.sendto(msg.encode(), (MULTICAST_ADDR, MULTICAST_PORT))
        print(f"sent multicast message: {msg}")

    def startListen(self):
        def _listenCast():
            while True:
                data, sender = self.castSocket.recvfrom(1024)
                senderAddr, senderPort = sender
                if senderAddr != self.localIp:
                    if data == b"stop":
                        print("received stop message")
                        self.notifications.put(("stop",))
                        return
                    else:
                        print("ignoring message from unknown sender")
                else:
                    self.notifications.put(
                        (data.decode(), senderAddr,  senderPort))

        self.castListenThread = Thread(target=_listenCast)
        self.castListenThread.start()

    def stopListen(self):
        self.castSocket.sendto("stop".encode(), (self.localIp, MULTICAST_PORT))
        self.castListenThread.join()

    def close(self):
        if self.castListenThread.is_alive():
            self.stopListen()
        self.castSocket.close()


class Node:
    def __init__(self):
        self.localIp = getMachineIp()

        # maximum number of incoming and outgoing connections
        self.maxIn = 10
        self.maxOut = 10

        # UDP/peers searching
        self.peers = NodeConnection(self.localIp)
        self.peersAware = True

        # thread locks
        self.serveConnLock = Lock()
        self.clientConnLock = Lock()
        self.portsLock = Lock()

        # signals
        self.serverManagerSignal = Semaphore(1)
        self.stopAdvertise = False
        self.stopServe = False

        # thread containers
        self.peerNotificationsCallbackThread: Thread = None
        self.serverManagerThread: Thread = None
        self.propogateDataThread: Thread = None
        self.advertiseThread: Thread = None

        self.availablePorts = dict()
        self.usedPorts = dict()

        self.servedConnections = dict()
        self.clientConnections = dict()

        self.dataPropogateQueue = Queue(self.maxIn + self.maxOut)
        self.localDataQueue = Queue((self.maxIn + self.maxOut)*2)

        # start handlers
        self._peerNotificationsHandler()
        self._manageServers()
        self._manageAdvertisers()
        self._propogateData()

    def _peerNotificationsHandler(self):
        def _callback():
            clientThreads = []
            while True:
                newNotificaion = self.peers.notifications.get()
                if newNotificaion == ("stop",):
                    break
                elif self.peersAware:
                    command, senderAddr, senderPort = newNotificaion
                    commandOperation, commandArgs = command.split(" ")
                    if commandOperation == "available":
                        if not type(commandArgs) == str:
                            continue
                        self.serveConnLock.acquire()
                        if senderAddr in self.servedConnections.keys():
                            continue
                        self.serveConnLock.release()
                        self.clientConnLock.acquire()
                        if senderAddr in self.clientConnections.keys():
                            continue
                        self.clientConnLock.release()
                        t = Thread(target=self.newClient,
                                   args=(senderAddr, int(commandArgs)))
                        t.start()
                        clientThreads.append(t)

            for t in clientThreads:
                if not t.is_alive():
                    continue
                t.join()
        self.peerNotificationsCallbackThread = Thread(target=_callback)
        self.peerNotificationsCallbackThread.start()

    def _shutdownSockets(self):
        self.portsLock.acquire()
        for port in self.availablePorts:
            socket(AF_INET, SOCK_DGRAM).connect((self.localIp, port))
        for conn in chain(self.availablePorts.values(), self.usedPorts.values()):
            try:
                conn.shutdown(SHUT_RDWR)
            except OSError as e:
                if e.args[0] == 107:
                    continue
            conn.close()
        self.portsLock.release()

    def _stopPeerNotifications(self):
        self.peers.close()
        self.peerNotificationsCallbackThread.join(3)

    def _manageAdvertisers(self):
        def _advertiseServers():
            while True:
                if self.stopAdvertise:
                    return
                self.portsLock.acquire()
                for port in self.availablePorts.keys():
                    try:
                        self.peers.cast(f"available {port}")
                    except OSError as e:
                        if e.args[0] == 9:
                            self.availablePorts.pop(port)
                            break
                self.portsLock.release()
                sleep(ADVERTISE_SERV_DELAY)

        self.advertiseThread = Thread(target=_advertiseServers)
        self.advertiseThread.start()

    def _generatePort(self):
        randomPort = randint(MULTICAST_PORT + 1, 65535)
        self.portsLock.acquire()
        while randomPort in self.availablePorts.keys() or randomPort in self.usedPorts.keys():
            randomPort = randint(MULTICAST_PORT + 1, 65535)
        self.portsLock.release()
        return randomPort

    def _manageServers(self):
        def _manageThreads():
            serverThreads: List[Thread] = []
            while len(self.availablePorts) + len(self.servedConnections) < self.maxIn:
                self.serverManagerSignal.acquire()
                if self.stopServe:
                    break
                newPort = self._generatePort()
                t = Thread(target=self.newServ, args=(newPort,))
                t.start()
                serverThreads.append(t)
            for t in serverThreads:
                if not t.is_alive():
                    continue
                t.join()

        self.serverManagerThread = Thread(target=_manageThreads)
        self.serverManagerThread.start()

    def _stopServerManager(self):
        self.stopServe = True
        self.stopAdvertise = True
        self.peersAware = False
        self.serverManagerSignal.release()
        self.advertiseThread.join()
        self.serverManagerThread.join()

    def dataSpread(self, data: str, origin=None):
        for addr, conn in chain(self.servedConnections.items(), self.clientConnections.items()):
            if addr == origin:
                continue
            try:
                conn.send(data.encode())
            except BrokenPipeError:
                pass

    def _propogateData(self):
        def _queueListener():
            while True:
                originAddr, newData = self.dataPropogateQueue.get()
                if originAddr is None and newData == "stop":
                    break
                if newData[0] == b"":
                    continue
                self.dataSpread(newData, originAddr)
                self.localDataQueue.put(newData)

        self.propogateDataThread = Thread(target=_queueListener)
        self.propogateDataThread.start()

    def _stopDataPropogator(self):
        self.dataPropogateQueue.put((None, "stop"))
        self.propogateDataThread.join()

    def close(self):
        self._shutdownSockets()
        self._stopServerManager()
        self._stopPeerNotifications()
        self._stopDataPropogator()

    def newServ(self, port):
        tcpSocket = socket(AF_INET, SOCK_STREAM)
        tcpSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        tcpSocket.bind(("0.0.0.0", port))
        tcpSocket.listen()

        self.portsLock.acquire()
        while True:
            self.availablePorts[port] = tcpSocket
            self.portsLock.release()

            try:
                clientConn, clientFullAddr = tcpSocket.accept()
                clientAddr, clientPort = clientFullAddr
            except OSError as e:
                if e.args[0] == 22:
                    break
                tcpSocket.close()
                break

            self.serverManagerSignal.release()
            self.portsLock.acquire()
            self.availablePorts.pop(port)
            self.usedPorts[port] = tcpSocket
            self.portsLock.release()
            self.serveConnLock.acquire()
            self.servedConnections[clientAddr] = clientConn
            self.serveConnLock.release()

            with clientConn:
                while True:
                    data = clientConn.recvfrom(1024)
                    if not data:
                        break
                    if data[0] == b"":
                        break
                    self.dataPropogateQueue.put((clientAddr, data))
            self.serveConnLock.acquire()
            self.servedConnections.pop(clientAddr)
            self.serveConnLock.release()
            self.portsLock.acquire()
            self.usedPorts.pop(port)
            self.portsLock.release()

    def newClient(self, addr, port: int):
        clientSock = socket(AF_INET, SOCK_STREAM)
        clientSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        with clientSock:
            try:
                self.portsLock.acquire()
                self.usedPorts[port] = clientSock
                self.portsLock.release()
                clientSock.connect((addr, port))
                self.clientConnLock.acquire()
                self.clientConnections[addr] = clientSock
                self.clientConnLock.release()

                while True:
                    data = clientSock.recvfrom(1024)
                    if not data:
                        break
                    if data[0] == b"":
                        break
                    self.dataPropogateQueue.put((addr, data))

            except ConnectionRefusedError as e:
                print(f"{e}")
            finally:
                self.clientConnLock.acquire()
                self.clientConnections.pop(addr)
                self.clientConnLock.release()
                self.portsLock.acquire()
                self.usedPorts.pop(port)
                self.portsLock.release()


if __name__ == "__main__":
    localNode = Node()
    def msgGetter(): return print(localNode.localDataQueue.get())
    msgThread = Thread(target=msgGetter, daemon=True)
    msgThread.start()

    while True:
        localNode.dataSpread(input("What data would you like to spread?: "))
    localNode.close()
