import sys
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication


class DashBoard(QMainWindow):
    def __init__(self, ponds=None):
        super().__init__()
        self.ponds = ponds
        self.__init_ui()

    def __init_ui(self):
        self.setGeometry(0, 20, 800, 200)
        self.setWindowTitle('Dashboard')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    d = DashBoard()
    app.exec_()