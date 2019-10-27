#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-24 22:19
# @Author  : zbz
# @Site    : 
# @File    : requests_control.py
# @Software: PyCharm

from brower_control import *

import requests
from user_agent import generate_user_agent
def get_current_cookies():
    session = initializeSession(database_config)
    cookies = session.query(Lscooky.cookies).order_by(Lscooky.id.desc()).first()
    return cookies[0]
def get_online_status(cookies):
    s = requests.session()
    s.cookies.update(cookies)
    s.headers.update({"user-agent": generate_user_agent()})
    online_status = s.get("http://pub.alimama.com/common/getUnionPubContextInfo.json")
    return online_status.text

def check_is_online(online_status):
    if "mmNick" in online_status:
        return True
    else:
        return False
if __name__ == '__main__':
    cookie = get_current_cookies()
    format_cookies_list = eval(str(cookie))
    format_cookies = {x["name"]: x["value"] for x in format_cookies_list}
    print(format_cookies)
    status = get_online_status(format_cookies)
    print(status)
