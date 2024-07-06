import logging
import os.path


class LogGen:

    def loggen(self):
        path = os.path.abspath(os.curdir)+'..\\logs\\automation.log'
        logging.basicConfig(filename=path,
                            format='%(pastime)s: %(levelness)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
