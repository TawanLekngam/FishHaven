from PySide6.QtCharts import QChart, QChartView, QPieSeries
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QVBoxLayout, QWidget

from FishSchool import FishSchool


class PieChartWidget(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.series = QPieSeries()

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle('Genesis')

        chart_view = QChartView(self.chart)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        layout = QVBoxLayout(self)
        layout.addWidget(chart_view)
        self.setLayout(layout)
        self.setFixedSize(400, 400)

    def update(self, fishes: FishSchool):
        series = QPieSeries()
        for key, value in fishes.get_items():
            series.append(key, len(value))
        self.chart.removeAllSeries()
        self.chart.addSeries(series)
