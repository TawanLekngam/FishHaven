from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QMainWindow, QScrollArea, QVBoxLayout, QWidget)

from config import WINDOW_SIZE
from FishSchool import FishSchool
from FishSchoolWidget import FishSchoolWidget
from LogDetailWidget import LogDetailWidget
from style import get_font

from PieChartWidget import PieChartWidget


class Dashboard(QMainWindow):
    def __init__(self, fish_school: FishSchool = None):
        super().__init__()
        self.__fish_school = fish_school

        FONT_BOLD_24 = get_font("Poppins", 22, bold=True)

        main_widget = QWidget(self)
        main_widget.setStyleSheet("border: 1px solid black;")

        main_widget_layout = QVBoxLayout(main_widget)
        main_widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        pie_chart = PieChartWidget(self, self.__fish_school)
        main_layout.addWidget(pie_chart)
        fish_school_widget = FishSchoolWidget(self, self.__fish_school)
        main_layout.addWidget(fish_school_widget)

        main_scroll_area = QScrollArea(self)
        main_scroll_area.setWidgetResizable(True)
        main_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        main_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        main_scroll_area.setWidget(main_widget)
        main_widget_layout.addLayout(main_layout) 

        side_widget = QWidget(self)
        side_layout = QVBoxLayout(side_widget)
        side_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        log_label = QLabel("Log")
        log_label.setFont(FONT_BOLD_24)
        log_label.setStyleSheet("background-color: #E5ECF6; border: 1px solid black;")
        side_layout.addWidget(log_label)

        log_scroll_area = QScrollArea(self)
        log_scroll_area.setWidgetResizable(True)
        log_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        log_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
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

    def add_log(self, log: LogDetailWidget):
        self.logs_container.layout().addWidget(log)
