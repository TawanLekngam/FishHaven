from typing import List

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QMainWindow, QScrollArea,
                               QVBoxLayout, QWidget)

from config import WINDOW_SIZE
from FishSchool import FishSchool
from FishSchoolWidget import FishSchoolWidget
from GenesisBarWidget import GenesisBarWidget
from LogDetailWidget import LogDetailWidget
from style import get_font


class Dashboard(QMainWindow):
    def __init__(self, fish_school: FishSchool = None):
        super().__init__()
        self.__fish_school = fish_school
        self.__log_list: List[LogDetailWidget] = []

        FONT_BOLD_20 = get_font("Poppins", 20, bold=True)

        main_widget = QWidget(self)
        main_widget.setStyleSheet("border: 1px solid black;")

        main_widget_layout = QVBoxLayout(main_widget)
        main_widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.genesis_bar = GenesisBarWidget(self, self.__fish_school)
        main_layout.addWidget(self.genesis_bar)

        self.fish_school_widget = FishSchoolWidget(self)
        main_layout.addWidget(self.fish_school_widget)

        main_scroll_area = QScrollArea(self)
        main_scroll_area.setWidgetResizable(True)
        main_scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        main_scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        main_scroll_area.setWidget(main_widget)
        main_widget_layout.addLayout(main_layout)

        side_widget = QWidget(self)
        side_layout = QVBoxLayout(side_widget)
        side_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        log_label = QLabel("Log")
        log_label.setFont(FONT_BOLD_20)
        log_label.setStyleSheet(
            "background-color: #E5ECF6; border: 1px solid black;")
        side_layout.addWidget(log_label)

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
        layout.addWidget(main_scroll_area)
        layout.addWidget(side_widget)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle("Dashboard")
        self.setFixedSize(WINDOW_SIZE[0], WINDOW_SIZE[1])

        timer = QTimer(self)
        timer.timeout.connect(self.__update)
        timer.start(1000)

    def add_log(self, log: LogDetailWidget):
        self.logs_container.layout().addWidget(log)
        self.__log_list.append(log)

    def __update(self):
        self.genesis_bar.update()
        for log in self.__log_list:
            log.update()
        self.fish_school_widget.update(self.__fish_school)
