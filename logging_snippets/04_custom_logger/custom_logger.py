import logging
import inspect

def customlogger(loglevel):
    # Get the name of the class/method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    # By default log all the messages
    logger.setLevel(logging.DEBUG)

    # filehandler
    filehandler = logging.FileHandler("{0}.log".format(logger_name), mode='w')
    filehandler.setLevel(loglevel)

    # formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    return logger