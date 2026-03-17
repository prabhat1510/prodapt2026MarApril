import logging
#logging.basicConfig(filename="mylog.txt",level=logging.DEBUG)   
logging.basicConfig(level=logging.INFO)
logging.critical("This is critical")
logging.info("Application started")
logging.warning("Low disk space")
logging.error("File not found")
