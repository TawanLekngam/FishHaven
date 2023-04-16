from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QScrollArea, QVBoxLayout,
                               QWidget)

import config
from FishSchool import FishSchool
from PieChartWidget import PieChartWidget
from PondInfoWidget import PondInfoWidget


class GenesisBarWidget(QWidget):
    def __init__(self, parent: QWidget, fishes: FishSchool):
        super().__init__(parent)
        self.__fishes = fishes

        frame = QFrame(self)
        frame_layout = QHBoxLayout(frame)
        frame_layout.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.pie_chart = PieChartWidget(self)
        frame_layout.addWidget(self.pie_chart)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        scroll_area_content = QWidget(self)
        scroll_area_content_layout = QHBoxLayout(scroll_area_content)
        scroll_area_content_layout.setContentsMargins(0, 0, 0, 0)
        scroll_area_content_layout.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        scroll_area_content.setLayout(scroll_area_content_layout)
        scroll_area.setWidget(scroll_area_content)
        frame_layout.addWidget(scroll_area)

        self.pond_info = PondInfoWidget(
            self, config.POND_NAME, self.__fishes.get_population())
        scroll_area_content_layout.addWidget(self.pond_info)

        for pond in config.OTHER_CHANNEL:
            other_pond_info = PondInfoWidget(self, pond)
            scroll_area_content_layout.addWidget(other_pond_info)

        layout = QVBoxLayout(self)
        layout.addWidget(frame)
        frame.setStyleSheet("border: 1px solid black;")
        self.setLayout(layout)

    def update(self):
        self.pie_chart.update(self.__fishes)
        self.pond_info.update(self.__fishes.get_population())
