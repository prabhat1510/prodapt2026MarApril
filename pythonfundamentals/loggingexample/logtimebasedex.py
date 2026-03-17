import logging
import logging.handlers
import time

# Create a logger
logger = logging.getLogger("MyLogger")
logger.setLevel(logging.INFO)

# Create a TimedRotatingFileHandler
# Rotates every minute ('M'), keeps 5 backup files
handler = logging.handlers.TimedRotatingFileHandler(
    'app.log', 
    when='M', 
    interval=1, 
    backupCount=5
)

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Log some messages to demonstrate
for i in range(10):
    logger.info(f"This is line {i} of the log file.")
    time.sleep(1) # Sleep to allow potential rollover in a real application
