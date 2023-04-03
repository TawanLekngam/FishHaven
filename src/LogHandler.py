from logging import Handler, LogRecord
from Dashboard import Dashboard
from LogDetail import LogDetail


class LogHandler(Handler):
    def __init__(self, dashboard: Dashboard):
        super().__init__()
        self.dashboard = dashboard

    def emit(self, record: LogRecord):
        log = LogDetail(record)
        self.dashboard.add_log(log)
