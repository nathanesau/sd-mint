# simple linux service to backup redis cache

from datetime import datetime
import os
import glob
import time
import shutil
from datetime import datetime

import logging
from logging.handlers import RotatingFileHandler

def backup_redis_task():
    logger.info("running backup redis task at {}".format(datetime.now()))

    ret_code = os.system("docker exec mint-redis redis-cli -a {} --rdb /data/dump.rdb".format(
        os.environ['REDIS_PASS']))
    if ret_code == 0:
        logger.info("backup successful")
    else:
        logger.info("unable to backup data")

# create logger
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

# create file handler and set level to debug
fh = RotatingFileHandler('/var/log/backup_redis.log', maxBytes=2000, backupCount=1)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

while True: # run task forever
    backup_redis_task()
    time.sleep(30)
