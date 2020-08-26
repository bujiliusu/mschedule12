import logging.handlers
import time
def getlogger(mod_name:str, filepath:str, level=logging.INFO, propagate=False):
    logger = logging.getLogger(mod_name)
    logger.setLevel(level)
    logger.propagate = propagate

    handler = logging.handlers.RotatingFileHandler(filepath, maxBytes=10*1024, backupCount=5)
    handler.setLevel(level)
    formatter = logging.Formatter(fmt="%(asctime)s %(name)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
if __name__ == '__main__':
    logger = getlogger('hello', 'd:/test/test.log')
    for i in range(1000):
        time.sleep(0.1)
        logger.info('i={}'.format(i))