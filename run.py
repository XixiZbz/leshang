#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-24 22:28
# @Author  : zbz
# @Site    : 
# @File    : main.py
# @Software: PyCharm


from requests_control import *

current_cookies = get_current_cookies()
if current_cookies:
    pass
else:
    format_cookies = get_cookies()
    store_cookies(format_cookies)