import sys
import time
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout)
from PySide6.QtCore import Qt

from components import PondWidget


class DashBoard(QMainWindow):
    __UPDATE_DELAY = 2

    def __init__(self, fishs: list = None):
        super().__init__()
        self.fishs = fishs
        self.__init_ui()

    def __init_ui(self):
        self.setFixedSize(1280, 720)
        self.setStyleSheet('background-color: white;')
        self.setWindowTitle("Pond Dashboard")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        self.pond_count = PondWidget(self, "Doo Pond", 3)
        self.last_update = time.time()

        layout.addWidget(self.pond_count)
        self.setLayout(layout)
        self.show()

    def update(self):
        current_time = time.time()
        if current_time - self.last_update < DashBoard.__UPDATE_DELAY:
            return
        self.last_update = current_time


if __name__ == "__main__":
    app = QApplication(sys.argv)
    d = DashBoard()
    app.exec()
