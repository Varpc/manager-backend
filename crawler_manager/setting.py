# -*- coding: utf-8 -*-


class Config:
    JISUANKE_UPDATE_INTERVAL = 3 * 3600  # 间隔三小时
    CODEFORCES_UPDATE_INTERVAL = 3 * 3600
    VJUDGE_UPDATE_INTERVAL = 24 * 3600
    WAIT_TIME = 10  # 请求失败重试等待时间
    TRY_TIME = 10  # 请求重试次数
