from logging import Handler, LogRecord

from Dashboard import Dashboard
from factories import logFactory


class LogHandler(Handler):
    def __init__(self, dashboard: Dashboard):
        super().__init__()
        self.dashboard = dashboard

    def emit(self, record: LogRecord):
        widget = logFactory.generate_log_widget(record)
        self.dashboard.add_log(widget)
