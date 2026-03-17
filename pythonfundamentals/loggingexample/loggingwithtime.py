import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="mylog.log"
)

logging.info("Application started")
logging.warning("CPU usage high")
logging.error("Database connection failed")
print(logging.basicConfig.__doc__)