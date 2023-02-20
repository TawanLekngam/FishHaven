from PySide6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QApplication, QFrame)
from PySide6.QtGui import QFont
from PySide6.QtCore import (QSize, Qt)


class PondWidget(QWidget):
    FONT_BOLD_36 = QFont('Poppins')
    FONT_BOLD_36.setPixelSize(36)
    FONT_BOLD_36.setBold(True)

    FONT_REG_24 = QFont('Poppins')
    FONT_REG_24.setPixelSize(24)

    def __init__(self, parent: QWidget, pond_name: str, fish_count: int = 0):
        super().__init__(parent)
        self.setFixedSize(QSize(150, 90))

        frame = QFrame(self)
        frame.setFixedSize(QSize(150, 90))
        frame.setStyleSheet('background-color:"#FFF3F1";border-radius:8;')
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        frame.setLayout(layout)

        self.pond_label = QLabel(pond_name, frame)
        self.pond_label.setFont(PondWidget.FONT_REG_24)
        self.pond_label.setStyleSheet('color:black;')
        self.pond_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.pond_label)

        self.count_label = QLabel(f"{fish_count}", frame)
        self.count_label.setFont(PondWidget.FONT_BOLD_36)
        self.count_label.setStyleSheet('color:black;')
        self.count_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.count_label)

    def update(self, fish_count: int):
        self.count_label.setText(f"{fish_count}")


if __name__ == '__main__':
    app = QApplication([])
    pond_name = 'Pond'
    fish_count = PondWidget(None, pond_name, 3)
    fish_count.show()
    app.exec()
