import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


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

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setGeometry(QRect(30, 30, 1381, 841))

        self.doo_pond_dashboard = DooPondDashboard(self, FONT_BOLD_24, FONT_REG_14)
        self.stackedWidget.addWidget(self.doo_pond_dashboard)

        self.show()


class DooPondDashboard(QWidget):
    def __init__(self, parent: QWidget = None, FONT_BOLD_24=None, FONT_REG_14=None):
        QWidget.__init__(self, parent)

        self.current_population = CurrentPopulation(
            self, FONT_BOLD_24, FONT_REG_14)
        self.current_population.setGeometry(QRect(0, 60, 201, 111))


class CurrentPopulation(QFrame):
    def __init__(self, parent: QFrame = None, FONT_BOLD_24=None, FONT_REG_14=None):
        QFrame.__init__(self, parent)

        self.setStyleSheet(
            "background-color: #FFF7F0; border-radius:10;")
        self.setObjectName("current_population")

        self.curr_pop_title = QLabel("Current Population", self)
        self.curr_pop_title.setObjectName("curr_pop_title")
        self.curr_pop_title.setGeometry(QRect(30, 30, 141, 20))
        self.curr_pop_title.setFont(FONT_REG_14)
        self.curr_pop_title.setStyleSheet("color: black;")
        self.curr_pop_title.setAlignment(Qt.AlignLeft)

        self.curr_pop_number = QLabel("0", self)
        self.curr_pop_number.setObjectName("curr_pop_number")
        self.curr_pop_number.setGeometry(QRect(30, 60, 91, 31))
        self.curr_pop_number.setFont(FONT_BOLD_24)
        self.curr_pop_number.setStyleSheet("color: black;")
        self.curr_pop_number.setAlignment(Qt.AlignLeft)

        self.curr_pop_rate = QLabel("0", self)
        self.curr_pop_rate.setObjectName("curr_pop_rate")
        self.curr_pop_rate.setGeometry(QRect(130, 67, 41, 16))
        self.curr_pop_rate.setFont(FONT_REG_14)
        self.curr_pop_rate.setStyleSheet("color: black;")
        self.curr_pop_rate.setAlignment(Qt.AlignRight)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    d = Dashboard()
    app.exec_()
