#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-24 23:03
# @Author  : zbz
# @Site    : 
# @File    : keep_online.py
# @Software: PyCharm
from brower_control import *
from requests_control import get_online_status,check_is_online
import logging
import time
format_cookies = get_cookies()
store_cookies(format_cookies)

status = get_online_status(format_cookies)

is_online = check_is_online(status)

count_num = 1

while 1:
    status = get_online_status(format_cookies)
    is_online = check_is_online(status)
    if is_online:
        time.sleep(60)
        logging.info("cookies 存活时长{num}分钟".format(num=count_num))
        count_num +=1
        continue
    else:
        logging.info("cookies 失效")
        format_cookies = get_cookies()
        store_cookies(format_cookies)
        continue