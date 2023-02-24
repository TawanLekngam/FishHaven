from PySide6.QtWidgets import QMainWindow

class KeeperPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1280, 720)
        self.setWindowTitle("Keeper Panel")


    def update(self):
        pass


    def set_add_button(self, func):
        ...