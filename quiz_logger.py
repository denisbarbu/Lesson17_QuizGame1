import logging
import coloredlogs
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO)
coloredlogs.install(level='DEBUG', logger=logger)



if __name__ == '__main__':

    logger.debug("Aici e un debug")
    logger.info("Aici e un info")
    logger.warning("Aici este un warning")
    logger.error("Aici este o eroare")