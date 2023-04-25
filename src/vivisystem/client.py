from typing import Callable, Dict

import socketio
from vivisystem.models import EventType, VivisystemFish, VivisystemPond


class VivisystemClient:
    def __init__(self, url, pond_id):
        self.pond_id = pond_id
        self.sio = socketio.Client()
        self.sio.connect(f"{url}?pondId={pond_id}", wait_timeout=5)
        self._handlers: Dict[EventType, Callable] = {
            EventType.STATUS: self.__status_handler,
            EventType.MIGRATE: self.__migration_handler,
            EventType.DISCONNECT: self.__disconnect_handler,
        }
        for event, handler in self._handlers.items():
            self.sio.on(event, handler)

    def disconnect(self):
        self.sio.disconnect()

    def handle_event(self, event: EventType, callback: Callable):
        self._handlers[event] = callback

    def send_status(self, pond: VivisystemPond):
        self.sio.emit(EventType.STATUS, pond._asdict())

    def migrate_fish(self, destination: str, fish: VivisystemFish):
        self.sio.emit(EventType.MIGRATE, data=(destination, fish._asdict()))

    def __status_handler(self, pond):
        pond = VivisystemPond(**pond)
        if pond.name == self.pond_id:
            return
        handle = self._handlers.get(EventType.STATUS)
        if handle:
            handle(pond)

    def __migration_handler(self, destination, fish):
        fish = VivisystemFish(**fish)
        if destination != self.pond_id:
            return
        handle = self._handlers.get(EventType.MIGRATE)
        if handle:
            handle(fish)

    def __disconnect_handler(self, pond_id: str):
        handle = self._handlers.get(EventType.DISCONNECT)
        if handle:
            handle(pond_id)
