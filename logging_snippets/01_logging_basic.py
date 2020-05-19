"""
5 levels of logging

DEBUG - To log debug messages (using for debugging code).
INFO -  To log messages stating that the system is working as expected.
WARNING - To log messages stating that the system is working fine as of now, but may not be so in near future due to some issue with syntax etc.
ERROR - To log messages where exception or error encountered.
CRITICAL -  To log messages regarding program entering into critical state and cannot go forward or exited from running.
"""


import logging

# By default if filename not given, logs to console
# logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s ', datefmt="%m/%d/%Y %I:%M:%S %p")

logging.basicConfig( filename='logs/sample_logger.txt',level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s ', datefmt="%m/%d/%Y %I:%M:%S %p")


logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")

