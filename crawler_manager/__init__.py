# -*- coding: utf-8 -*-

from crawler_manager.setting import Config
import requests, time, threading

config = Config()


# UpdateTimeIntervalApi调用更改当前配置
def change_update_callback(*args, **kwargs):
    global config
    if kwargs.get('jisuanke'):
        config.JISUANKE_UPDATE_INTERVAL = kwargs.get('jisuanke')
    if kwargs.get('codeforces'):
        config.CODEFORCES_UPDATE_INTERVAL = kwargs.get('codeforces')
    if kwargs.get('vjudge'):
        config.VJUDGE_UPDATE_INTERVAL = kwargs.get('vjudge')
    if kwargs.get('wait_time'):
        config.WAIT_TIME = kwargs.get('wait_time')
    if kwargs.get('try_time'):
        config.TRY_TIME = kwargs.get('try_time')


def update_jisuanke(port=5000):
    global config
    url = 'http://127.0.0.1:%s/update/jisuanke' % port
    while True:
        try_time = config.TRY_TIME
        while 200 != requests.get(url).status_code and try_time > 0:
            try_time = try_time - 1
            time.sleep(config.WAIT_TIME)
        time.sleep(config.JISUANKE_UPDATE_INTERVAL)


def update_codeforces(port=5000):
    global config
    url = 'http://127.0.0.1:%s/update/codeforces' % port
    while True:
        try_time = config.TRY_TIME
        while 200 != requests.get(url).status_code and try_time > 0:
            try_time = try_time - 1
            time.sleep(config.WAIT_TIME)
        time.sleep(config.CODEFORCES_UPDATE_INTERVAL)


def crawler_manager(port):
    global config
    url = 'http://127.0.0.1:%s/api/admin/crawler/time' % port
    try_time = config.TRY_TIME
    while requests.get(url).status_code != 200 and try_time > 0:
        try_time = try_time - 1
        time.sleep(config.WAIT_TIME)

    jisuanke_thread = threading.Thread(target=update_jisuanke, args=(port,))
    codeforces_thread = threading.Thread(target=update_codeforces, args=(port,))
    jisuanke_thread.start()
    codeforces_thread.start()
    jisuanke_thread.join()
    codeforces_thread.join()
