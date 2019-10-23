#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-16 20:42
# @Author  : zbz
# @Site    : 
# @File    : test.py
# @Software: PyCharm

from selenium import webdriver
import requests
browser = webdriver.Ie()
url = "https://login.taobao.com/member/login.jhtml?style=mini&newMini2=true&from=alimama&redirectURL=http%3A%2F%2Flogin.taobao.com%2Fmember%2Ftaobaoke%2Flogin.htm%3Fis_login%3d1&full_redirect=true"
browser.get(url)
button = browser.find_element_by_xpath("//button[contains(text(),'登 录')]")
print(button)
button.click()
cookies = browser.get_cookies()
browser.close()

format_cookies_list = eval(cookies)
format_cookies = {x["name"]:x["value"] for x in cookies}



# with open("./cookies",'r') as f:
#     cookies = f.read()

tb_token= format_cookies[' _tb_token_']
s = requests.session()
s.cookies.update(cookies)
url = "https://pub.alimama.com/report/getCPPaymentDetails.json?t=1571668389426&_tb_token_={tb_token}&startTime=2019-10-15&endTime=2019-10-21&payStatus=&queryType=1&toPage=1&perPageSize=40&positionIndex=&jumpType=0".format(tb_token)
res = s.get(url)
print(res.text)
