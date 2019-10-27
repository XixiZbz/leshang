#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-16 20:42
# @Author  : zbz
# @Site    : 
# @File    : test.py
# @Software: PyCharm

from selenium import webdriver
import requests
from model import Lscooky, initializeSession

database_config = {'user': 'root', 'password': '123456', 'host': '47.75.155.126',
                   'port': 3306, 'db': 'leShang', 'charset': 'utf8mb4'}



# with open("./cookies",'r') as f:
#     cookies = f.read()

# tb_token= format_cookies['_tb_token_']
# s = requests.session()
# s.cookies.update(format_cookies)
# url = "https://pub.alimama.com/report/getCPPaymentDetails.json?t=1571668389426&_tb_token_={tb_token}&startTime=2019-10-15&endTime=2019-10-21&payStatus=&queryType=1&toPage=1&perPageSize=40&positionIndex=&jumpType=0".format(tb_token=tb_token)
# res = s.get(url)
# print(res.text)
