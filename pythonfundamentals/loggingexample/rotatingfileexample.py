'''
Example: File Logging with Size-Based Rotation
The following example sets up a logger that writes to app.log. The log file will roll over when it reaches 500 bytes, keeping up to 2 backup files (named app.log.1, app.log.2, etc.).
RotatingFileHandler restricts file growth by creating backups (app.log.1, etc.) when maxBytes is reached.
'''
import logging
from logging.handlers import RotatingFileHandler
import time

# Configure logger
logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)

# Setup handler with 500-byte limit and 2 backups
handler = RotatingFileHandler('rapp.log', maxBytes=500, backupCount=2)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Generate logs to trigger rotation
for i in range(150):
    logger.info(f"Log message {i}")

