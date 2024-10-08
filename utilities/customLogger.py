import logging


class LogGen:
    @staticmethod
    def loggen():
        path = '..\\logs\\automation.log'
        logging.basicConfig(filename=path,
                            format='%(pastime)s: %(levelness)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
