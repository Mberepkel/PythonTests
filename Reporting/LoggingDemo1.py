import logging
logging.basicConfig(filename="log.1",
                    format= "%(asctime)s : %(levelname)s : %(message)s",
                    datefmt='%d/%m/%Y %I:%M:%S:%p', level=logging.DEBUG
                    )
## you can also specify directory of another location you want the log to be created if not on same folder

logging.debug("this is a debug")
logging.info("this is for info")

logging.warning("this is for warning")
logging.critical("this is a critical message")
logging.error("this is for error message")
