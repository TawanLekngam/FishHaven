import sys
import time
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QLabel)
from PySide6.QtCore import (QRect)
from PySide6.QtGui import QFont

from components import PondWidget


class DashBoard(QMainWindow):
    def __init__(self, fishs: list = None):
        super().__init__()
        self.fishs = fishs
        self.__init_ui()

    def __init_ui(self):

        FONT_BOLD_36 = QFont('Poppins')
        FONT_BOLD_36.setPixelSize(36)
        FONT_BOLD_36.setBold(True)

        self.setFixedSize(1280, 720)
        self.setStyleSheet('background-color: white;')
        self.setWindowTitle("Pond Dashboard")

        title = QLabel('Fish Haven Dashboard', self)
        title.setGeometry(QRect(80, 50, 641, 51))
        title.setFont(FONT_BOLD_36)
        title.setStyleSheet('color: black;')

        self.dp = PondWidget(self, "Doo Pond")
        self.dp.setGeometry(QRect(80, 140, 231, 231))

        self.last_update = time.time()

    def update(self, **kwargs):
        current_time = time.time()
        if current_time - self.last_update < 1:
            return
        self.last_update = current_time

        if "doo_pond" in kwargs:
            self.dp.update(kwargs["doo_pond"])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    d = DashBoard()
    app.exec()
