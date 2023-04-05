from logging import Handler, LogRecord
from Dashboard import Dashboard
from LogDetailWidget import LogDetailWidget


class LogHandler(Handler):
    def __init__(self, dashboard: Dashboard):
        super().__init__()
        self.dashboard = dashboard

    def emit(self, record: LogRecord):
        if record.name == "pond":
            log = LogDetailWidget(record, "fish")
        else:
            log = LogDetailWidget(record)
        self.dashboard.add_log(log)
