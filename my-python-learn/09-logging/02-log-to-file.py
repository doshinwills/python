import logging

logging.basicConfig(filename="logging.log", level=logging.DEBUG)

# Default is Warn level
logging.error("Error")
logging.critical("critical")
logging.warning("warning")
logging.info("info")
logging.debug("debug")
