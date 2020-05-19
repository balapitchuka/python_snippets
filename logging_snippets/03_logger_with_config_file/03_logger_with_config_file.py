import logging
import logging.config

class LoggerExampleConf:

    def test_log(self):

        # logger
        # create logger, all messages will be logged as records by logger
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerExampleConf.__name__)
        

        # log messages
        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")
        logger.critical("critical message")


log_obj = LoggerExampleConf()
log_obj.test_log()
