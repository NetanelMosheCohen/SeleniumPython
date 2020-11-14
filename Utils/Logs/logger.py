import logging

logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler("Utils\\Logs\\automation.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s.%(funcName)s - %(message)s')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.setLevel(logging.INFO)
