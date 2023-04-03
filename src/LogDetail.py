from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtGui import QFont
from logging import LogRecord
from time import time


class LogDetail(QWidget):
    def __init__(self, record: LogRecord):
        super().__init__()
        self.record = record

        self.image_label = QLabel(self)
        self.image_label.setFixedSize(54, 54)
        self.image_label.setStyleSheet(
            "background-color:#E5ECF6; border-radius: 10px")

        self.description_label = QLabel(self.record.getMessage(), self)
        self.description_label.setFont(QFont("Arial", 14))
        self.description_label.setAlignment(Qt.AlignLeft)

        self.time_label = QLabel(self.calculate_time(), self)
        self.time_label.setFont(QFont("Arial", 12))
        self.time_label.setAlignment(Qt.AlignLeft)
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
