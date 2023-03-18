from PySide6.QtWidgets import (QMainWindow, QApplication, QFrame, QLabel, QPushButton, QGridLayout, QScrollArea, )
from PySide6.QtGui import QFont

class KeeperPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1280, 720)
        self.setWindowTitle("Keeper Panel")
        self.__init_ui();


    def __init_ui(self):
        self.__init_keeper_panel()
        self.__init_keeper_list()


    def __init_keeper_panel(self):
        self.keeper_panel = QFrame(self)
        self.keeper_panel.setFixedSize(1280, 720)
        self.keeper_panel.setStyleSheet('background-color: white;')

        self.keeper_panel_title = QLabel('Keeper Panel', self.keeper_panel)
        self.keeper_panel_title.setGeometry(80, 50, 641, 51)
        self.keeper_panel_title.setFont(QFont('Poppins', 36, QFont.Bold))
        self.keeper_panel_title.setStyleSheet('color: black;')

        self.keeper_panel_add_button = QPushButton('Add', self.keeper_panel)
        self.keeper_panel_add_button.setGeometry(80, 120, 100, 30)
        self.keeper_panel_add_button.setFont(QFont('Poppins', 12, QFont.Bold))
        self.keeper_panel_add_button.setStyleSheet('color: black;')

    def __init_keeper_list(self):
        self.keeper_list = QScrollArea(self)
        self.keeper_list.setFixedSize(1280, 720)
        self.keeper_list.setStyleSheet('background-color: white;')
        self.keeper_list.setGeometry(0, 0, 1280, 720)

        self.keeper_list_content = QFrame(self.keeper_list)
        self.keeper_list_content.setFixedSize(1280, 720)
        self.keeper_list_content.setStyleSheet('background-color: white;')

        self.keeper_list.setWidget(self.keeper_list_content)
        self.keeper_list.setWidgetResizable(True)

        self.keeper_list_layout = QGridLayout(self.keeper_list_content)
        self.keeper_list_layout.setContentsMargins(0, 0, 0, 0)
        self.keeper_list_layout.setSpacing(0)

        self.keeper_list_content.setLayout(self.keeper_list_layout)

        self.keeper_list_content.hide()

    def update(self):
        pass


    def set_add_button(self, func):
        ...



if __name__ == "__main__":
    app = QApplication([])
    k = KeeperPanel()
    k.show()
    app.exec()
