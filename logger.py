import logging
from datetime import datetime
import pytz
from logging.handlers import TimedRotatingFileHandler

# Set up the loggig services
# Create a logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create a file handler
# file_handler = TimedRotatingFileHandler('./logs/logs.log', when='midnight', interval=1, backupCount=365)
#
# file_handler.setLevel(logging.DEBUG)
#
# # Create a format for the logs
# formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', '%Y-%m-%d %H:%M:%S %Z%z')
# file_handler.setFormatter(formatter)
#
# # Add the file handler to the logger
# logger.addHandler(file_handler)



# #For logging to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a formatter for the log messages
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Add the formatter to the console handler
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)