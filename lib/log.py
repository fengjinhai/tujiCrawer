#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import time
import os


MON_STR = time.strftime('%Y-%m',time.localtime(time.time()))
DAY_STR = time.strftime('%Y-%m-%d-%H-%M',time.localtime(time.time()))

log_file_pre = time.strftime('crawer_%Y-%m-%d-%H',time.localtime(time.time()))
log_folder = '../log/' + MON_STR + '/'

if os.path.exists(log_folder) == False:
    os.makedirs(log_folder)
log_file_name = log_folder + log_file_pre + '.log'

def init_log(log_file_name=log_file_name, level=9):
    logger = logging.getLogger()
    hdlr = logging.FileHandler(log_file_name)
    if level == 0:
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(process)d][%(thread)d][%(filename)s:%(funcName)s:%(lineno)s]::%(message)s')
    else:
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(process)d][%(filename)s:%(lineno)s]::%(message)s')

    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.NOTSET)
    return logger

global logger
logger = init_log()
