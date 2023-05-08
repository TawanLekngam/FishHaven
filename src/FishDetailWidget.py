from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget

from FishSprite import FishSprite
from helper import surface_to_pixmap


class FishDetailWidget(QWidget):
    def __init__(self, parent: QWidget, fish: FishSprite):
        super().__init__(parent)
        self.__fish = fish

        frame = QFrame(self)
        frame_layout = QVBoxLayout(frame)

        image_label = QLabel(frame)
        image_label.setAlignment(Qt.AlignCenter)
        pixmap = surface_to_pixmap(self.__fish.get_image())
        image_label.setPixmap(pixmap)

        id_label = QLabel(f"ID: {self.__fish.get_id()}", frame)
        parent_id_label = QLabel(
            f"Parent ID: {self.__fish.get_parent_id()}", frame)
        genesis_label = QLabel(f"Genesis: {self.__fish.get_genesis()}", frame)
        pheromone_text = f"Pheromone: {self.__fish.get_pheromone()}/{self.__fish.get_pheromone_threshold()}"
        pheromone_label = QLabel(pheromone_text, frame)
        age_text = f"Age: {self.__fish.get_age()}/{self.__fish.get_lifespan()}"
        age_label = QLabel(age_text, frame)

        frame_layout.addWidget(image_label)
        frame_layout.addWidget(id_label)
        frame_layout.addWidget(parent_id_label)
        frame_layout.addWidget(genesis_label)
        frame_layout.addWidget(pheromone_label)
        frame_layout.addWidget(age_label)

        layout = QVBoxLayout(self)
        layout.addWidget(frame)
        frame.setStyleSheet("border: 1px solid black; border-radius:5px; background-color: white;")

        self.setFixedSize(150, 300)
        self.setLayout(layout)


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = FishDetailWidget()
    sys.exit(app.exec_())
