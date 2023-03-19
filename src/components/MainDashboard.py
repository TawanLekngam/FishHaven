import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


from DPDashboard import DPDashboard

"""Main Dashboard"""


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

        self.doo_pond_dashboard = DPDashboard(self)
        self.stackedWidget.addWidget(self.doo_pond_dashboard)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    d = Dashboard()
    app.exec_()
