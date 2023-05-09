import matplotlib.pyplot as plt
import pyqtgraph as pg
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QGridLayout, QLabel, QListWidget,QMainWindow, QPushButton, QScrollArea, QVBoxLayout, QWidget)



class ViviDashboard(QMainWindow):
    def __init__(self, connected_pond):
        super().__init__()
        self.connected_ponds = connected_pond
        self.label = QLabel(self)
        self.list_widget = QListWidget(self)
        self.initUI()

        timer = QTimer(self)
        timer.timeout.connect(self.update_dashboard)
        timer.start(1000)

    def update_dashboard(self):
        temp = self.connected_ponds.values()
        self.list_widget.clear()
        for items in temp:
            
            self.list_widget.addItem(str(items))


    def graph(self):
        matrix_pond = [1, 2, 5]
        time = list(range(0, len(matrix_pond)))
        plt.plot(time, matrix_pond)

        plt.xlabel("Time")
        plt.ylabel("Amount of Fish")

        plt.title("Ponds Graph")
        plt.show()

    def graph_pyqt(self):
        matrix_pond = [1, 2, 5]
        otherpond = [0, len(self.client.other_ponds), 3]
        time = list(range(0, len(matrix_pond)))
        plot = pg.plot()
        plot.showGrid(x=True, y=True)
        plot.addLegend()
        plt.setXRange(0, 10)

        plt.setYRange(0, 20)

        plt.setWindowTitle("Pond Dashboard")

        matrix_pond_line = plot.plot(time, matrix_pond)
        otherpond_line = plot.plot(time, otherpond)

    def initUI(self):
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout(self.widget)
        self.grid = QGridLayout()
        self.graph_button = QPushButton("Graph")

        font = QFont('Arial', 20, QFont.Bold)
        self.label.setFont(font)
        self.connectLabel = QLabel("Connected Ponds:", self.widget)
        self.connectLabel.setFont(font)

        self.vbox.addWidget(self.connectLabel)
        self.vbox.addWidget(self.list_widget)
        self.vbox.addLayout(self.grid)
        self.widget.setLayout(self.vbox)

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)
        self.setGeometry(0, 20, 800, 300)
        self.setWindowTitle("Vivisystem Dashboard")
    def update(self):
        pass