from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QGridLayout, QScrollArea, QVBoxLayout, QWidget

from FishDetailWidget import FishDetailWidget
from FishSchool import FishSchool


class FishSchoolWidget(QWidget):
    COL = 8

    def __init__(self, parent, fishes: FishSchool):
        super().__init__(parent)
        self.__fishes = fishes
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        scroll_area = QScrollArea(self)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget(scroll_area)
        self.scroll_widget.setLayout(self.grid_layout)
        scroll_area.setWidget(self.scroll_widget)

        layout = QVBoxLayout(self)
        layout.addWidget(scroll_area)
        self.setLayout(layout)
        self.setStyleSheet("border: 1px solid black;")

        self.setFixedHeight(500)

        timer = QTimer(self)
        timer.timeout.connect(self.__update)
        timer.start(1000)

    def __update(self):
        while self.grid_layout.count():
            child = self.grid_layout.takeAt(0)
            widget = child.widget()
            if widget is not None:
                widget.deleteLater()

        row = 0
        col = 0

        for fish in self.__fishes.get_fishes():
            fish_widget = FishDetailWidget(self, fish)
            self.grid_layout.addWidget(fish_widget, row, col)
            col += 1
            if col == FishSchoolWidget.COL:
                col = 0
                row += 1
