from PySide6.QtWidgets import QWidget, QHBoxLayout, QScrollArea, QFrame
from InfoWidget import InfoWidget
from FishSchool import FishSchool
from PySide6.QtCore import Qt

class GenesisBarWidget(QWidget):
    def __init__(self, parent: QWidget = None, fish_scool: FishSchool = None):
        super().__init__(parent)
        self.__fish_school = fish_scool
        
        main_layout = QHBoxLayout(self)
        self.fish_count = InfoWidget(self, "All Fish", 0)
        main_layout.addWidget(self.fish_count, alignment=Qt.AlignmentFlag.AlignLeft)

        self.genesis_scroll_area = QScrollArea(self)
        self.genesis_scroll_area.setWidgetResizable(True)
        self.genesis_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.genesis_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        main_layout.addWidget(self.genesis_scroll_area)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    widget = GenesisBarWidget()
    widget.show()
    sys.exit(app.exec_())
