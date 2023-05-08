import os.path as path
from logging import LogRecord
from time import time

from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout, QWidget

from config import ASSET_DIR
from style import get_font

ICON_DIR = path.join(ASSET_DIR, "log-icon")


class LogDetailWidget(QWidget):
    def __init__(self, record: LogRecord, icon: str = None):
        super().__init__()
        self.record = record

        FONT_BOLD_14 = get_font("Poppins", 14, bold=True)
        FONT_REG_12 = get_font("Poppins", 12)

        frame = QFrame(self)
        frame.setFrameShape(QFrame.Panel)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setFixedHeight(80)
        frame.setStyleSheet("background-color: white; border-radius: 5px;")

        self.image_label = QLabel(frame)
        self.image_label.setFixedSize(54, 54)
        self.image_label.setStyleSheet("background-color: white;")

        if icon:
            image = QImage(path.join(ICON_DIR, f"{icon}.png"))
            pixmap = QPixmap.fromImage(image).scaled(50, 50)
            self.image_label.setPixmap(pixmap)

        self.description_label = QLabel(frame)
        self.description_label.setFont(FONT_BOLD_14)
        self.description_label.setText(record.msg)
        self.description_label.setStyleSheet("color: black;")
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.time_label = QLabel(frame)
        self.time_label.setFont(FONT_REG_12)
        self.time_label.setText(self.calculate_time())
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.time_label.setStyleSheet("color: gray;")

        layout = QHBoxLayout(frame)
        layout.addWidget(self.image_label)
        layout.addSpacing(10)

        inner_layout = QVBoxLayout()
        inner_layout.addWidget(self.description_label)
        inner_layout.addWidget(self.time_label)
        layout.addLayout(inner_layout)

        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(frame)

    def update(self):
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
