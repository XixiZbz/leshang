#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-23 23:40
# @Author  : zbz
# @Site    : 
# @File    : get_cookies.py
# @Software: PyCharm

from selenium import webdriver
from model import Lscooky, initializeSession
database_config = {'user': 'root', 'password': '123456', 'host': '47.75.155.126',
                   'port': 3306, 'db': 'leShang', 'charset': 'utf8mb4'}

browser = webdriver.Ie()
url = "https://login.taobao.com/member/login.jhtml?style=mini&newMini2=true&from=alimama&redirectURL=http%3A%2F%2Flogin.taobao.com%2Fmember%2Ftaobaoke%2Flogin.htm%3Fis_login%3d1&full_redirect=true"
browser.get(url)
button = browser.find_element_by_xpath("//button[contains(text(),'登 录')]")
print(button)
button.click()
cookies = browser.get_cookies()
browser.close()
print(cookies)
format_cookies_list = eval(str(cookies))
format_cookies = {x["name"]:x["value"] for x in cookies}

session = initializeSession(database_config)
session.add(Lscooky(cookies=str(format_cookies)))

session.commit()