import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class InfoFrame(QFrame):
    def __init__(self, parent=None, color=None, x=None, y=None, name=None):
        super().__init__(parent)

        self.setGeometry(QRect(x, y, 201, 111))
        self.setStyleSheet(f"background-color: {color}; border-radius: 10px;")
        self.setObjectName(name)

        FONT_BOLD_24 = QFont('Poppins')
        FONT_BOLD_24.setPixelSize(24)
        FONT_BOLD_24.setBold(True)

        FONT_REG_14 = QFont('Poppins')
        FONT_REG_14.setPixelSize(14)

        self.title_label = QLabel(name.replace('_', ' ').title(), self)
        self.title_label.setObjectName(f"{name}_title")
        self.title_label.setGeometry(QRect(30, 30, 141, 20))
        self.title_label.setFont(FONT_REG_14)
        self.title_label.setStyleSheet("color: black;")
        self.title_label.setAlignment(Qt.AlignLeft)

        self.number_label = QLabel("0", self)
        self.number_label.setObjectName(f"{name}_number")
        self.number_label.setGeometry(QRect(30, 60, 91, 31))
        self.number_label.setFont(FONT_BOLD_24)
        self.number_label.setStyleSheet("color: black;")
        self.number_label.setAlignment(Qt.AlignLeft)

        self.rate_label = QLabel("0", self)
        self.rate_label.setObjectName(f"{name}_rate")
        self.rate_label.setGeometry(QRect(130, 67, 41, 16))
        self.rate_label.setFont(FONT_REG_14)
        self.rate_label.setStyleSheet("color: black;")
        self.rate_label.setAlignment(Qt.AlignRight)
