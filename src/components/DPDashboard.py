import time
from PySide6.QtWidgets import QWidget, QFrame, QLabel, QScrollArea, QWidget, QVBoxLayout
from PySide6.QtCore import QRect
from PySide6.QtGui import Qt, QFont

import logging
from typing import List


FONT_BOLD_24 = QFont('Poppins')
FONT_BOLD_24.setPixelSize(24)
FONT_BOLD_24.setBold(True)

FONT_REG_14 = QFont('Poppins')
FONT_REG_14.setPixelSize(14)

FONT_REG_12 = QFont('Poppins')
FONT_REG_12.setPixelSize(12)


class DPDashboard(QWidget):
    """Dashboard for the Doo Pond"""

    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)

        self.population = InfoFrame(
            self, '#FFF7F0', 0, 60, 'current_population')

        self.dead_fishes = InfoFrame(self, '#EEF1FF', 230, 60, 'dead_fishes')

        self.male_fishes = InfoFrame(self, '#F0FAFF', 460, 60, 'male_fishes')

        self.female_fishes = InfoFrame(
            self, '#FFF3F1', 690, 60, 'female_fishes')

        self.population_trend = PopulationTrend(self)
        self.population_trend.setGeometry(QRect(0, 200, 891, 361))

        self.genesis = Genesis(self)
        self.genesis.setGeometry(QRect(0, 590, 431, 251))

        self.move_stress = InfoFrame(self, '#FFF7F0', 460, 590, 'move_stress')

        self.move_instinct = InfoFrame(
            self, '#EEF1FF', 690, 590, 'move_instinct')

        self.death_god = InfoFrame(self, '#F0FAFF', 460, 730, 'death_god')

        self.death_disaster = InfoFrame(
            self, '#FFF3F1', 690, 730, 'death_disaster')

        self.line = QFrame(self)
        self.line.setGeometry(QRect(906, 0, 1, 852))
        self.line.setStyleSheet("background-color:gray;")
        self.line.setFrameShape(QFrame.VLine)

        self.pond_log = PondLog(self)
        self.pond_log.setGeometry(QRect(920, 0, 461, 841))

    def update(self, data: int):
        self.population.set_number(str(data))
        self.pond_log.update()


class PopulationTrend(QFrame):
    def __init__(self, parent: QFrame) -> None:
        QFrame.__init__(self, parent)

        self.setStyleSheet(
            "border:2px solid; border-color: #F7F9FB; border-radius:10;")


class Genesis(QFrame):
    def __init__(self, parent: QFrame) -> None:
        QFrame.__init__(self, parent)

        self.setStyleSheet(
            "border:2px solid; border-color: #F7F9FB; border-radius:10;")


class PondLog(QFrame):
    def __init__(self, parent: QFrame) -> None:
        QFrame.__init__(self, parent)

        self.setStyleSheet("border:none;")

        self.title = QLabel("Pond Log", self)
        self.title.setGeometry(QRect(0, 10, 81, 20))
        self.title.setFont(FONT_REG_14)
        self.title.setStyleSheet("color: black;")
        self.title.setAlignment(Qt.AlignLeft)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setGeometry(QRect(0, 40, 461, 801))
        self.scrollArea.setStyleSheet("border:none;")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 461, 801))

        self.vbox = QVBoxLayout()
        self.vbox.setAlignment(Qt.AlignTop)

        self.scrollAreaWidgetContents.setLayout(self.vbox)
        self.scrollAreaWidgetContents.layout().setContentsMargins(0, 1, 0, 1)
        self.scrollAreaWidgetContents.layout().setSpacing(0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.log_details: List[LogDetail] = []
        self.logger = logging.getLogger("pond")

        handler = PondLogHandler(self)
        handler.setLevel(logging.DEBUG)
        self.logger.addHandler(handler)

    def add_log(self, record: logging.LogRecord) -> None:
        log_detail = LogDetail(self.scrollAreaWidgetContents, record)
        self.log_details.append(log_detail)
        self.scrollAreaWidgetContents.layout().addWidget(log_detail)
        self.scrollArea.verticalScrollBar().setValue(
            self.scrollArea.verticalScrollBar().maximum())

    def update(self) -> None:
        for log_detail in self.log_details:
            log_detail.update()


class PondLogHandler(logging.Handler):
    def __init__(self, pond_log: PondLog) -> None:
        logging.Handler.__init__(self)
        self.pond_log = pond_log

    def emit(self, record: logging.LogRecord) -> None:
        self.pond_log.add_log(record)


class InfoFrame(QFrame):
    def __init__(self, parent=None, color=None, x=None, y=None, name=None):
        super().__init__(parent)

        self.setGeometry(QRect(x, y, 201, 111))
        self.setStyleSheet(f"background-color: {color}; border-radius: 10px;")

        FONT_BOLD_24 = QFont('Poppins')
        FONT_BOLD_24.setPixelSize(24)
        FONT_BOLD_24.setBold(True)

        FONT_REG_14 = QFont('Poppins')
        FONT_REG_14.setPixelSize(14)

        self.title_label = QLabel(name.replace('_', ' ').title(), self)
        self.title_label.setGeometry(QRect(30, 30, 141, 20))
        self.title_label.setFont(FONT_REG_14)
        self.title_label.setStyleSheet("color: black;")
        self.title_label.setAlignment(Qt.AlignLeft)

        self.number_label = QLabel("0", self)
        self.number_label.setGeometry(QRect(30, 60, 91, 31))
        self.number_label.setFont(FONT_BOLD_24)
        self.number_label.setStyleSheet("color: black;")
        self.number_label.setAlignment(Qt.AlignLeft)

        self.rate_label = QLabel("0", self)
        self.rate_label.setGeometry(QRect(130, 67, 41, 16))
        self.rate_label.setFont(FONT_REG_14)
        self.rate_label.setStyleSheet("color: black;")
        self.rate_label.setAlignment(Qt.AlignRight)

    def set_number(self, number: str):
        self.number_label.setText(number)

    def set_rate(self, rate: str):
        self.rate_label.setText(rate)


class LogDetail(QFrame):
    def __init__(self, parent: QFrame, record: logging.LogRecord):
        QFrame.__init__(self, parent)
        self.setFixedSize(461, 81)
        self.setStyleSheet("border:none;")
        self.record = record

        self.image_frame = QFrame(self)
        self.image_frame.setGeometry(QRect(10, 13, 54, 54))
        self.image_frame.setStyleSheet(
            "background-color:#E5ECF6;  border-radius:10;")

        self.description = QLabel(self.record.getMessage(), self)
        self.description.setGeometry(QRect(80, 20, 371, 20))
        self.description.setFont(FONT_REG_14)
        self.description.setStyleSheet("color: black;")
        self.description.setAlignment(Qt.AlignLeft)

        self.time = QLabel(f"{self.calculate(self.record.created)} ago", self)
        self.time.setGeometry(QRect(80, 40, 371, 20))
        self.time.setFont(FONT_REG_12)
        self.time.setStyleSheet("color: gray;")

    def update(self) -> None:
        self.time.setText(f"{self.calculate(self.record.created)} ago")

    def calculate(self, created_time: float) -> str:
        current_time = time.time()
        time_diff = current_time - created_time
        if time_diff < 60:
            return f"{int(time_diff)}s"
        elif time_diff < 3600:
            return f"{int(time_diff // 60)}m"
        elif time_diff < 86400:
            return f"{int(time_diff // 3600)}h"
        else:
            return f"{int(time_diff // 86400)}d"
