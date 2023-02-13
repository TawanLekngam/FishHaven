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

        # Khor Pond
        kp_box = QWidget(self)
        kp_box.setGeometry(QRect(330, 140, 231, 231))
        kp_box.setStyleSheet('background-color:"#FFF3F1"; border-radius:8;')

        kp_title = QLabel('Khor Pond', kp_box)
        kp_title.setGeometry(QRect(20, 60, 191, 31))
        kp_title.setFont(FONT_REG_24)
        kp_title.setStyleSheet('color:black;')
        kp_title.setAlignment(Qt.AlignCenter)

        self.kp_fish = QLabel('0', kp_box)
        self.kp_fish.setObjectName('kp_fish')
        self.kp_fish.setGeometry(QRect(20, 130, 191, 41))
        self.kp_fish.setFont(FONT_BOLD_36)
        self.kp_fish.setStyleSheet('color:black;')
        self.kp_fish.setAlignment(Qt.AlignCenter)
        
        # Auay Pond
        ap_box = QWidget(self)
        ap_box.setGeometry(QRect(80, 400, 231, 231))
        ap_box.setStyleSheet('background-color:"#FFF3F1"; border-radius:8;')

        ap_title = QLabel('Auay Pond', ap_box)
        ap_title.setGeometry(QRect(20, 60, 191, 31))
        ap_title.setFont(FONT_REG_24)
        ap_title.setStyleSheet('color:black;')
        ap_title.setAlignment(Qt.AlignCenter)

        self.ap_fish = QLabel('0', ap_box)
        self.ap_fish.setObjectName('ap_fish')
        self.ap_fish.setGeometry(QRect(20, 130, 191, 41))
        self.ap_fish.setFont(FONT_BOLD_36)
        self.ap_fish.setStyleSheet('color:black;')
        self.ap_fish.setAlignment(Qt.AlignCenter)

        # Mega Pond
        mgp_box = QWidget(self)
        mgp_box.setGeometry(QRect(330, 400, 231, 231))
        mgp_box.setStyleSheet('background-color:"#EEF1FF";border-radius:8;')

        mgp_title = QLabel('Mega Pond', mgp_box)
        mgp_title.setGeometry(QRect(20, 60, 191, 31))
        mgp_title.setFont(FONT_REG_24)
        mgp_title.setStyleSheet('color:black;')
        mgp_title.setAlignment(Qt.AlignCenter)

        self.mgp_fish = QLabel('0', mgp_box)
        self.mgp_fish.setObjectName('mgp_fish')
        self.mgp_fish.setGeometry(QRect(20, 130, 191, 41))
        self.mgp_fish.setFont(FONT_BOLD_36)
        self.mgp_fish.setStyleSheet('color:black;')
        self.mgp_fish.setAlignment(Qt.AlignCenter)

        self.show()

    def set_dp_fish(self, amount: int) -> None:
        self.dp_fish.setText(amount)

    def set_kp_fish(self, amount: int) -> None:
        self.kp_fish.setText(amount)

    def set_ap_fish(self, amount: int) -> None:
        self.ap_fish.setText(amount)
    
    def set_mgp_fish(self, amount: int) -> None:
        self.mgp_fish.setText(amount)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    d = DashBoard()
    app.exec_()
