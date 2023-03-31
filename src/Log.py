from logging import (CRITICAL, DEBUG, ERROR, INFO, WARNING, Formatter, Logger,
                     LogRecord, StreamHandler, getLogger)


class CustomFormatter(Formatter):
    GREY = "\x1b[38;20m"
    BLUE = "\x1b[34;20m"
    YELLOW = "\x1b[33;20m"
    RED = "\x1b[31;20m"
    RESET = "\x1b[0m"
    FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    def __init__(self, fmt=FORMAT, datefmt="%H:%M:%S"):
        super().__init__(fmt, datefmt)

    def format(self, record: LogRecord):
        log_fmt = self.GREY + self.FORMAT + self.RESET
        if record.levelno == DEBUG:
            log_fmt = self.BLUE + self.FORMAT + self.RESET
        elif record.levelno == WARNING:
            log_fmt = self.YELLOW + self.FORMAT + self.RESET
        elif record.levelno in (ERROR, CRITICAL):
            log_fmt = self.RED + self.FORMAT + self.RESET
            if record.levelno == CRITICAL:
                log_fmt = self.RED + self.FORMAT + self.RESET
        elif record.levelno == INFO:
            log_fmt = self.GREY + self.FORMAT + self.RESET
        formatter = Formatter(log_fmt, datefmt=self.datefmt)
        return formatter.format(record)


def get_logger(name: str = None) -> Logger:
    logger = getLogger(name)
    logger.setLevel(DEBUG)
    ch = StreamHandler()
    ch.setLevel(DEBUG)
    ch.setFormatter(CustomFormatter())
    logger.addHandler(ch)
    return logger
