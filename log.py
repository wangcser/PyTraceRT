import logging
import logging
import time


class LOG:
    def __init__(self, log_file=None):
        self.logger = logging.getLogger("logger")
        formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")

        if log_file is None:
            stime = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
            log_file = "./result/tr_" + stime + ".log"
        else:
            log_file = log_file

        self.handler1 = logging.StreamHandler()
        self.handler2 = logging.FileHandler(filename=log_file)

        self.logger.setLevel(logging.DEBUG)
        self.handler1.setLevel(logging.DEBUG)
        self.handler2.setLevel(logging.DEBUG)

        self.handler1.setFormatter(formatter)
        self.handler2.setFormatter(formatter)

        self.logger.addHandler(self.handler1)
        self.logger.addHandler(self.handler2)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def debug(self, msg):
        self.logger.debug(msg)


log = LOG()
