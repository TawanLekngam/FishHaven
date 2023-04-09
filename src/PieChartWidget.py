import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import QMainWindow, QApplication ,QWidget, QVBoxLayout
from PySide6.QtCharts import QChart, QChartView, QPieSeries

from FishSchool import FishSchool

class PieChartWidget(QWidget):

    def __init__(self, parent: QWidget, fishes: FishSchool):
        super().__init__(parent)
        self.__fishes = fishes

        self.series = QPieSeries()
        for key, value in self.__fishes.get_items():
            self.series.append(key, len(value))


        print(self.series.count())

        # self.slice1 = self.series.slices()[0]
        # self.slice1.setLabelVisible()
        # self.slice1.setPen(QPen(Qt.darkGreen, 2))
        # self.slice1.setBrush(Qt.green)

        

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle('Genesis Chart')

        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        layout = QVBoxLayout(self)
        layout.addWidget(self._chart_view)
        self.setLayout(layout)
        self.setFixedSize(400, 400)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.__update)
        self.timer.start(1000)

    def __update(self):
        series = QPieSeries()
        for key, value in self.__fishes.get_items():
            series.append(key, len(value))

        self.chart.removeAllSeries()
        self.chart.addSeries(series)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PieChartWidget()
    window.show()
    window.resize(440, 300)

    sys.exit(app.exec())