import logging

class LoggerExample:

    def test_log(self):

        # logger
        # create logger, all messages will be logged as records by logger
        logger = logging.getLogger(LoggerExample.__name__)
        logger.setLevel(logging.INFO)

        # handler (outputs to console, file etc)
        # create console handler and set level info
        # stream handler for console printing
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s - %(message)s ', datefmt="%m/%d/%Y %I:%M:%S %p")

        # add formatter to console handler -> chandler
        chandler.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(chandler)

        # log messages
        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")
        logger.critical("critical message")


log_obj = LoggerExample()
log_obj.test_log()
