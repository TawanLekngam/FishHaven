import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

'''
dp = Doo Pond
kp = Khor Pond
ap = Auay Pond
mgp = Mega Pond
ag = Aqua Gang
mtp = Matrix Pond
'''

class DashBoard(QMainWindow):
    def __init__(self, ponds=None):
        super().__init__()
        self.ponds = ponds
        self.__init_ui()

    def __init_ui(self):
        self.setFixedSize(1440, 1048)
        self.setStyleSheet('background-color: white;')
        self.setWindowTitle('Doo Pond Dashboard')

        # Font
        FONT_BOLD_36 = QFont('Poppins')
        FONT_BOLD_36.setPixelSize(36)
        FONT_BOLD_36.setBold(True)

        FONT_REG_24 = QFont('Poppins')
        FONT_REG_24.setPixelSize(24)

        # Title
        title = QLabel('Fish Haven Vivisystem Dashboard', self)
        title.setGeometry(QRect(80, 50, 641, 51))
        title.setFont(FONT_BOLD_36)
        title.setStyleSheet('color: black;')

        # Doo Pond
        dp_box = QWidget(self)
        dp_box.setGeometry(QRect(80, 140, 231, 231))
        dp_box.setStyleSheet('background-color:"#EEF1FF";border-radius:8;')

        dp_title = QLabel('Doo Pond', dp_box)
        dp_title.setGeometry(QRect(20, 60, 191, 31))
        dp_title.setFont(FONT_REG_24)
        dp_title.setStyleSheet('color:black;')
        dp_title.setAlignment(Qt.AlignCenter)

        self.dp_fish = QLabel('0', dp_box)
        self.dp_fish.setObjectName('dp_fish')
        self.dp_fish.setGeometry(QRect(20, 130, 191, 41))
        self.dp_fish.setFont(FONT_BOLD_36)
        self.dp_fish.setStyleSheet('color:black;')
        self.dp_fish.setAlignment(Qt.AlignCenter)
        
        self.show()

    def set_dp_fish(self, amount: int) -> None:
        self.dp_fish.setText(amount)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    d = DashBoard()
    app.exec_()
