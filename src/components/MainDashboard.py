import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


from .DPDashboard import DPDashboard

"""Main Dashboard"""


class MainDashboard(QMainWindow):
    def __init__(self, ponds=None):
        super().__init__()
        self.ponds = ponds
        self.__init_ui()

    def __init_ui(self):
        self.setFixedSize(1440, 900)
        self.setStyleSheet('background-color: white;')
        self.setWindowTitle('Dashboard')

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setGeometry(QRect(30, 30, 1381, 841))

        self.doo_pond_dashboard = DPDashboard(self)
        self.stackedWidget.addWidget(self.doo_pond_dashboard)
        # self.show()

    def update(self, dp_data: list = None):
        self.doo_pond_dashboard.update(dp_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    d = MainDashboard()
    app.exec_()
