import logging
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPlainTextEdit


class QTextEditHandler(logging.Handler):
    def __init__(self, parent=None):
        super().__init__()
        self.widget = QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)
