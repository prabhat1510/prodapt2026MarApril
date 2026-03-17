'''
import logging

logger = logging.getLogger("MyApp")

logging.basicConfig(level=logging.INFO)

logger.info("Application started")
logger.error("Payment failed")
'''
import logging

logging.basicConfig(level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log")

def divide(a, b):

    logging.debug(f"Dividing {a} by {b}")

    try:
        result = a / b
        logging.info(f"Result = {result}")
        return result

    except ZeroDivisionError:
        logging.error("Division by zero error")

divide(10,2)
divide(10,0)
