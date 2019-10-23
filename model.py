#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-23 23:21
# @Author  : zbz
# @Site    : 
# @File    : model.py
# @Software: PyCharm

import yaml
from sqlalchemy import Column, String, create_engine, Integer, DATE, Numeric, Text, DATETIME, DateTime, text
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.pool import NullPool




def initializeSession(database_config):
    # 初始化数据库连接:
    engine_config = 'mysql+pymysql://{user}:{pw}@{host}:{port}/{db}?charset=utf8'
    engine = create_engine(engine_config.format(user=database_config['user'], pw=database_config['password'], \
                                                host=database_config['host'], port=database_config['port'], \
                                                db=database_config['db'],echo=True),poolclass=NullPool)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    session = scoped_session(DBSession)
    return session
Base = declarative_base()

class Lscooky(Base):
    __tablename__ = 'lscookies'

    id = Column(Integer, primary_key=True)
    cookies = Column(Text, nullable=False)
    gmt_create = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    gmt_modified = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))