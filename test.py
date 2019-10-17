#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-16 20:42
# @Author  : zbz
# @Site    : 
# @File    : test.py
# @Software: PyCharm

from selenium import webdriver

browser = webdriver.Ie()
url = "https://login.taobao.com/member/login.jhtml?style=mini&newMini2=true&from=alimama&redirectURL=http%3A%2F%2Flogin.taobao.com%2Fmember%2Ftaobaoke%2Flogin.htm%3Fis_login%3d1&full_redirect=true"
browser.get(url)
button = browser.find_element_by_xpath("//button[contains(text(),'登 录')]")
print(button)
button.click()
cookies = browser.get_cookies()
print(cookies)

with open("./cookies.txt",'w') as f:
    f.write(cookies)
