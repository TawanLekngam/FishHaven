from logging import LogRecord
from time import time
import os.path as path

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QWidget

from style import get_font

from config import ASSET_DIR


ICON_DIR = path.join(ASSET_DIR, "log-icon")


class LogDetailWidget(QWidget):
    def __init__(self, record: LogRecord, icon: str = None):
        super().__init__()

        FONT_BOLD_14 = get_font("Poppins", 14, bold=True)
        FONT_REG_12 = get_font("Poppins", 12)
        self.record = record

        self.image_label = QLabel(self)
        self.image_label.setFixedSize(54, 54)
        self.image_label.setStyleSheet("background-color:#E5ECF6; border-radius: 10px")

        if icon:
            image = QImage(path.join(ICON_DIR, f"{icon}.png"))
            pixmap = QPixmap.fromImage(image).scaled(50, 50)
            self.image_label.setPixmap(pixmap)

        self.description_label = QLabel(self.record.getMessage(), self)
        self.description_label.setFont(FONT_BOLD_14)
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.time_label = QLabel(self.calculate_time(), self)
        self.time_label.setFont(FONT_REG_12)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.time_label.setStyleSheet("color: gray;")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.__update)
        self.timer.start(1000)

        layout = QHBoxLayout(self)
        layout.addWidget(self.image_label)
        layout.addSpacing(10)

        inner_layout = QVBoxLayout()
        inner_layout.addWidget(self.description_label)
        inner_layout.addWidget(self.time_label)
        layout.addLayout(inner_layout)

        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        self.setFixedHeight(80)

    def __update(self):
        time_diff = self.calculate_time()
        self.time_label.setText(time_diff)

    def calculate_time(self):
        created_time = self.record.created
        current_time = time()
        time_diff = current_time - created_time
        if time_diff < 60:
            return f"{int(time_diff)}s ago"

        elif time_diff < 3600:
            return f"{int(time_diff // 60)}m ago"
        elif time_diff < 86400:
            return f"{int(time_diff // 3600)}h ago"
        else:
            return f"{int(time_diff // 86400)}d ago"
