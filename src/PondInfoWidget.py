from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

from style import get_font

class PondInfoWidget(QWidget):
    def __init__(self, parent=None, pond_name: str="Pond Name", population: int=0):
        super().__init__(parent)
        self.__name = pond_name

        FONT_REG_22 = get_font("Poppins", 22)
        FONT_REG_18 = get_font("Poppins", 18)

        frame = QFrame(self)
        frame_layout = QVBoxLayout(frame)

        frame_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)

        pond_name_label = QLabel(self.__name)
        pond_name_label.setFont(FONT_REG_22)
        frame_layout.addWidget(pond_name_label)

        self.population_label = QLabel(f"Population: {population}")
        self.population_label.setFont(FONT_REG_18)
        frame_layout.addWidget(self.population_label)
        
        layout = QVBoxLayout(self)
        layout.addWidget(frame)
        frame.setStyleSheet("border: 1px solid black;")

        # self.setFixedHeight(400)
        self.setLayout(layout)

    def update(self, population: int):
        self.population_label.setText(f"Population: {population}")



if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = PondInfoWidget()
    window.show()
    sys.exit(app.exec())