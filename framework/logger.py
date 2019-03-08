# -*- coding utf-8 -*-
import logging
import time
import os

class Logger(object):
    def __init__(self,logger):

        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        date=time.strftime("%Y%d%m%H%M",time.localtime(time.time()))

        log_path=os.path.dirname(os.path.abspath("."))+'/logs/'
        log_name=log_path+date+'.log'

        fh=logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        fomater=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(fomater)
        ch.setFormatter(fomater)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def getLog(self):
        return self.logger

