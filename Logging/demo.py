import logging
logging.basicConfig(filename ="test.log", level =logging.ERROR,
                    format ="%(asctime)s-%(levelname)s,%(message)s")
logger = logging.getLogger(__name__)

handler = logging.FileHandler('top.log')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.debug("test the customer logger")
