import sys
import logging
from PySide6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
from PySide6.QtCore import Qt

from QTextEditHandler import QTextEditHandler

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.log_widget = QPlainTextEdit(self)
        self.log_widget.setReadOnly(True)
        self.setCentralWidget(self.log_widget)
        logging.getLogger().addHandler(QTextEditHandler(self.log_widget))
        logging.getLogger().setLevel(logging.DEBUG)

        # Example logging statements
        logging.debug('Debug message')
        logging.info('Info message')
        logging.warning('Warning message')
        logging.error('Error message')
        logging.critical('Critical message')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
