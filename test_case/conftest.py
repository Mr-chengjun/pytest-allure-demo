import pytest
import config
import requests
import time

from config import user_conf
from utils import md5_hex
from urllib.parse import urljoin


@pytest.fixture(scope="session")
def login():
    url = urljoin(config.BASE_URL, 'dologin')
    secret_key = user_conf.SECRET_KEY
    api_token = user_conf.API_TOKEN
    time_stamp = str(int(time.time()))
    strs = secret_key + api_token + time_stamp
    Signature = md5_hex(strs)
    # 'Authorizationtoken': '',
    headers = {
        'Timestamp': time_stamp,
        'APIToken': api_token,
        'Signature': Signature,

    }
    data = {
        'username': user_conf.USER,
        'password': user_conf.PASSWORD
    }
    # res = requests.post(url=url, data=data, headers=headers)
    print("登录成功")
    return 123
    # print(res.)


@pytest.fixture(scope="function")
def headers():
    secret_key = user_conf.SECRET_KEY
    api_token = user_conf.API_TOKEN
    time_stamp = str(int(time.time()))
    strs = secret_key + api_token + time_stamp
    Signature = md5_hex(strs)
    header = {
        'Timestamp': time_stamp,
        'APIToken': api_token,
        'Signature': Signature,
    }
    return header


import logging


@pytest.fixture()
def log():
    logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                        filename='new.log',
                        filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                        # a是追加模式，默认如果不写的话，就是追加模式
                        format=
                        '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                        # 日志格式
                        )
