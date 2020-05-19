import logging
import custom_logger as c_log

class CustomLoggerExample:
    logger = c_log.customlogger(logging.DEBUG)

    def method1(self):
        self.logger.debug('debug message')
        self.logger.info('info message')
        self.logger.warn('warn message')
        self.logger.error('error message')
        self.logger.critical('critical message')

    def method2(self):
        m2Log = c_log.customlogger(logging.INFO)
        m2Log.debug('debug message')
        m2Log.info('info message')
        m2Log.warn('warn message')
        m2Log.error('error message')
        m2Log.critical('critical message')
    
    def method3(self):
        m3Log = c_log.customlogger(logging.INFO)
        m3Log.debug('debug message')
        m3Log.info('info message')
        m3Log.warn('warn message')
        m3Log.error('error message')
        m3Log.critical('critical message')


custom_log = CustomLoggerExample()
custom_log.method1()
custom_log.method2()
custom_log.method3()