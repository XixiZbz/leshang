#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-16 20:42
# @Author  : zbz
# @Site    : 
# @File    : test.py
# @Software: PyCharm

from selenium import webdriver

browser = webdriver.Ie()
url = "https://pub.alimama.com/report/getTbkPaymentDetails.json?startTime=2017-05-22&endTime=2017-08-19&payStatus=&queryType=1&toPage=1&perPageSize=20&total=&t=1503223605295&pvid=&_tb_token_=pTK7Mfldfvq&_input_charset=utf-8"
browser.get(url)
cookies = browser.get_cookies()
print(cookies)
