import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from info import InfoFrame


class Dashboard(QMainWindow):
    def __init__(self, ponds=None):
        super().__init__()
        self.ponds = ponds
        self.__init_ui()

    def __init_ui(self):
        self.setFixedSize(1440, 900)
        self.setStyleSheet('background-color: white;')
        self.setWindowTitle('Dashboard')

        # Font
        FONT_BOLD_24 = QFont('Poppins')
        FONT_BOLD_24.setPixelSize(24)
        FONT_BOLD_24.setBold(True)

        FONT_REG_14 = QFont('Poppins')
        FONT_REG_14.setPixelSize(14)

        FONT_REG_12 = QFont('Poppins')
        FONT_REG_12.setPixelSize(12)

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setGeometry(QRect(30, 30, 1381, 841))

        self.doo_pond_dashboard = DooPondDashboard(
            self, FONT_BOLD_24, FONT_REG_14, FONT_REG_12)
        self.stackedWidget.addWidget(self.doo_pond_dashboard)

        self.show()


class DooPondDashboard(QWidget):
    def __init__(self, parent: QWidget = None, FONT_BOLD_24=None, FONT_REG_14=None, FONT_REG_12=None):
        QWidget.__init__(self, parent)

        self.current_population = InfoFrame(
            self, '#FFF7F0', 0, 60, 'current_population')

        self.dead_fishes = InfoFrame(self, '#EEF1FF', 230, 60, 'dead_fishes')

        self.male_fishes = InfoFrame(self, '#F0FAFF', 460, 60, 'male_fishes')

        self.female_fishes = InfoFrame(self, '#FFF3F1', 690, 60, 'female_fishes')

        self.population_trend = PopulationTrend(
            self, FONT_BOLD_24, FONT_REG_14)
        self.population_trend.setGeometry(QRect(0, 200, 891, 361))

        self.genesis = Genesis(self, FONT_BOLD_24, FONT_REG_14)
        self.genesis.setGeometry(QRect(0, 590, 431, 251))

        self.move_stress = InfoFrame(self, '#FFF7F0', 460, 590, 'move_stress')

        self.move_instinct = InfoFrame(self, '#EEF1FF', 690, 590, 'move_instinct')

        self.death_god = InfoFrame(self, '#F0FAFF', 460, 730, 'death_god')

        self.death_disaster = InfoFrame(self, '#FFF3F1', 690, 730, 'death_disaster')


        self.line = QFrame(self)
        self.line.setGeometry(QRect(906, 0, 1, 852))
        self.line.setStyleSheet("background-color:gray;")
        self.line.setFrameShape(QFrame.VLine)

        self.pond_log = PondLog(self, FONT_REG_14, FONT_REG_12)
        self.pond_log.setGeometry(QRect(920, 0, 461, 841))


class PopulationTrend(QFrame):
    def __init__(self, parent: QFrame, FONT_BOLD_24=None, FONT_REG_14=None) -> None:
        QFrame.__init__(self, parent)

        self.setStyleSheet(
            "border:2px solid; border-color: #F7F9FB; border-radius:10;")
        self.setObjectName("population_trend")


class Genesis(QFrame):
    def __init__(self, parent: QFrame, FONT_BOLD_24=None, FONT_REG_14=None) -> None:
        QFrame.__init__(self, parent)

        self.setStyleSheet(
            "border:2px solid; border-color: #F7F9FB; border-radius:10;")
        self.setObjectName("genesis")


class PondLog(QFrame):
    def __init__(self, parent: QFrame, FONT_REG_14=None, FONT_REG_12=None) -> None:
        QFrame.__init__(self, parent)

        self.setStyleSheet(
            "border:none;")
        self.setObjectName("pond_log")

        self.pond_log_title = QLabel("Pond Log", self)
        self.pond_log_title.setObjectName("pond_log_title")
        self.pond_log_title.setGeometry(QRect(0, 10, 81, 20))
        self.pond_log_title.setFont(FONT_REG_14)
        self.pond_log_title.setStyleSheet("color: black;")
        self.pond_log_title.setAlignment(Qt.AlignLeft)

        self.pond_log_scrollArea = QScrollArea(self)
        self.pond_log_scrollArea.setObjectName("pond_log_scrollArea")
        self.pond_log_scrollArea.setGeometry(QRect(0, 40, 461, 801))
        self.pond_log_scrollArea.setStyleSheet("border:none;")
        self.pond_log_scrollArea.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        self.pond_log_scrollArea.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)

        self.pond_log_scrollAreaWidgetContents = QWidget()
        self.pond_log_scrollAreaWidgetContents.setObjectName(
            "pond_log_scrollAreaWidgetContents")
        self.pond_log_scrollAreaWidgetContents.setGeometry(
            QRect(0, 0, 461, 801))

        self.vbox = QVBoxLayout()
        self.vbox.setAlignment(Qt.AlignTop)

        self.pond_log_scrollAreaWidgetContents.setLayout(self.vbox)
        self.pond_log_scrollAreaWidgetContents.layout().setContentsMargins(0, 0, 0, 0)
        self.pond_log_scrollAreaWidgetContents.layout().setSpacing(0)
        self.pond_log_scrollArea.setWidget(
            self.pond_log_scrollAreaWidgetContents)

        # Add more logs here
        self.log_details1 = LogDetails(
            self.pond_log_scrollAreaWidgetContents, FONT_REG_14, FONT_REG_12, "Fish 0012 died")
        self.log_details2 = LogDetails(
            self.pond_log_scrollAreaWidgetContents, FONT_REG_14, FONT_REG_12, "Fish 1234 moved")

        self.pond_log_scrollAreaWidgetContents.layout().addWidget(self.log_details1)
        self.pond_log_scrollAreaWidgetContents.layout().addWidget(self.log_details2)


class LogDetails(QFrame):
    def __init__(self, parent: QFrame, FONT_REG_14=None, FONT_REG_12=None, description=str) -> None:
        QFrame.__init__(self, parent)
        self.setFixedSize(461, 81)
        self.setStyleSheet(
            "border:none;")
        self.setObjectName("log_details")

        self.image_frame = QFrame(self)
        self.image_frame.setObjectName("image_frame")
        self.image_frame.setGeometry(QRect(10, 13, 54, 54))
        self.image_frame.setStyleSheet(
            "background-color:#E5ECF6;  border-radius:10;")

        self.description = QLabel(description, self)
        self.description.setObjectName("description")
        self.description.setGeometry(QRect(80, 20, 371, 20))
        self.description.setFont(FONT_REG_14)
        self.description.setStyleSheet("color: black;")
        self.description.setAlignment(Qt.AlignLeft)

        self.time = QLabel("...m ago", self)
        self.time.setObjectName("time")
        self.time.setGeometry(QRect(80, 40, 371, 20))
        self.time.setFont(FONT_REG_12)
        self.time.setStyleSheet("color: gray;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    d = Dashboard()
    app.exec_()
