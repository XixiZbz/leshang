#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-16 20:42
# @Author  : zbz
# @Site    : 
# @File    : test.py
# @Software: PyCharm

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://pub.alimama.com/')
cookies = browser.get_cookies()
print(cookies)
