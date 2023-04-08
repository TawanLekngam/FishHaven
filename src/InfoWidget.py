from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget

from style import get_font


class InfoWidget(QWidget):
    def __init__(self, parent, title: str, count: int | str):
        super().__init__(parent)
        FONT_BOLD_24 = get_font("Poppins", 24, bold=True)
        FONT_BOLD_14 = get_font("Poppins", 14, bold=True)

        frame = QFrame(self)
        frame.setFixedSize(200, 100)
        frame.setFrameShape(QFrame.Box)
        frame.setLineWidth(1)

        title_label = QLabel(title, frame)
        title_label.setFont(FONT_BOLD_14)
        title_label.setAlignment(Qt.AlignLeft)

        self.count_label = QLabel(f"{count}", frame)
        self.count_label.setFont(FONT_BOLD_24)
        self.count_label.setAlignment(Qt.AlignLeft)

        layout = QVBoxLayout(frame)
        layout.addWidget(title_label)
        layout.addWidget(self.count_label)

        self.setObjectName("InfoWidget")
        self.setFixedSize(200, 80)

    def set_count(self, count: int | str):
        self.count_label.setText(f"{count}")


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    widget = InfoWidget(None, "test", "test")
    widget.show()
    sys.exit(app.exec_())
