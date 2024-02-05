from queue import Queue
from socket import (
    socket,
    AF_INET,
    SOCK_DGRAM,
    SOL_SOCKET,
    SO_REUSEADDR,
    IPPROTO_IP,
    IP_MULTICAST_TTL,
    IP_ADD_MEMBERSHIP,
    inet_aton)
from threading import Thread

MULTICAST_ADDR = "224.0.0.10"
MULTICAST_PORT = 49152


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
        self.notifs = Queue(10)
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
                        self.notifs.put(("stop",))
                        return
                    else:
                        print("ignoring message from unknown sender")
                else:
                    self.notifs.put((data.decode(), senderAddr,  senderPort))

        self.castListenThread = Thread(target=_listenCast)
        self.castListenThread.start()

    def stopListen(self):
        self.castSocket.sendto("stop".encode(), (self.localIp, MULTICAST_PORT))
        self.castListenThread.join()

    def close(self):
        if self.castListenThread.is_alive():
            self.stopListen()
        self.castSocket.close()
