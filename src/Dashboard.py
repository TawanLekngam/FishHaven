import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
                               QVBoxLayout, QWidget, QScrollArea)

from config import WINDOW_SIZE
from LogDetail import LogDetail
from FishSchool import FishSchool


class Dashboard(QMainWindow):
    def __init__(self, fish_school: FishSchool = None):
        super().__init__()
        self.fish_school = fish_school

        # Create main frame widget
        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)
        main_layout.addWidget(
            QLabel("Main Frame", alignment=Qt.AlignmentFlag.AlignCenter))
        main_widget.setStyleSheet("border: 1px solid black;")

        # Create side frame widget
        side_widget = QWidget(self)
        side_layout = QVBoxLayout(side_widget)

        log_label = QLabel("Log")
        log_label.setFont(QFont("Arial", 16))
        log_label.setStyleSheet(
            "background-color: #E5ECF6; border: 1px solid black;")
        side_layout.addWidget(log_label, alignment=Qt.AlignmentFlag.AlignTop)

        log_scroll_area = QScrollArea(self)
        log_scroll_area.setWidgetResizable(True)
        log_scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        log_scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        side_layout.addWidget(log_scroll_area)

        self.logs_container = QWidget(self)
        logs_container_layout = QVBoxLayout(self.logs_container)
        logs_container_layout.setContentsMargins(0, 0, 0, 0)
        logs_container_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        logs_container_layout.setSpacing(0)
        log_scroll_area.setWidget(self.logs_container)

        window_width = self.geometry().width()
        side_widget.setMaximumWidth(window_width * 0.5)

        side_widget.setStyleSheet("border: 1px solid black;")

        layout = QHBoxLayout()
        layout.addWidget(main_widget)
        layout.addWidget(side_widget)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle("Dashboard")
        self.setFixedSize(WINDOW_SIZE[0], WINDOW_SIZE[1])

    def add_log(self, log: LogDetail):
        self.logs_container.layout().addWidget(log)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    sys.exit(app.exec())
