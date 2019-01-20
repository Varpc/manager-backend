# -*- coding: utf-8 -*-

from manager.extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from manager.settings import BaseConfig


class Root(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    board = db.Column(db.Text)  # 首页公告板内容
    image = db.relationship('Image', back_populates='root')
    jisuanke_update_time = db.Column(db.DateTime, default=datetime.now)
    codeforces_update_time = db.Column(db.DateTime, default=datetime.now)
    jisuanke_update_interval = db.Column(db.Integer, default=3 * 60 * 60)  # 计蒜客爬虫更新时间间隔(单位s)
    codeforces_update_interval = db.Column(db.Integer, default=3 * 60 * 60)  # Codeforces爬虫更新时间间隔
    vjudge_update_interval = db.Column(db.Integer, default=24 * 60 * 60)  # vjudge爬虫更新时间间隔
    wait_time = db.Column(db.Integer, default=10)  # 爬虫爬取失败等待时间
    try_time = db.Column(db.Integer, default=10)  # 爬虫重试次数


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256), default=BaseConfig.DEFAULT_HOME_IMAGE_URI)
    root_id = db.Column(db.Integer, db.ForeignKey('root.id'))
    root = db.relationship('Root', back_populates='image')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    class_ = db.Column(db.String(200), nullable=False)  # 加下划线与关键字不重复
    image = db.Column(db.String(256), default=BaseConfig.DEFAULT_HEAD_IMAGE_URI)
    username = db.Column(db.String(256), nullable=False, unique=True)
    password_hash = db.Column(db.String(256))
    is_admin = db.Column(db.Boolean, default=False)
    vjid = db.Column(db.String(200))

    # 外键
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    group = db.relationship('Group', back_populates='member')
    #
    problems = db.relationship('Problems', back_populates='user', uselist=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


class Problems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    class_ = db.Column(db.String(200), nullable=False)
    count = db.Column(db.Integer, default=0)
    blue_book = db.Column(db.Integer, default=0)
    purple_book = db.Column(db.Integer, default=0)
    sum = db.Column(db.Integer, default=0)
    uva = db.Column(db.Integer, default=0)
    hdu = db.Column(db.Integer, default=0)
    poj = db.Column(db.Integer, default=0)
    cf = db.Column(db.Integer, default=0)
    bc = db.Column(db.Integer, default=0)
    status = db.Column(db.Integer, default=0)  # 0审核 1现役 2退役 3除名

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='problems')


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    no = db.Column(db.String(200), unique=True, index=True)
    member = db.relationship('User', back_populates='group')


# 近期比赛模型
class JiSuanKe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(200), nullable=False)
    contest = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(256), nullable=False)
    begin_time = db.Column(db.String(200), nullable=False)
    time = db.Column(db.String(200), nullable=False)


class Codeforces(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contest = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(256), nullable=False)
    writer = db.Column(db.String(200), default='')
    begin_time = db.Column(db.String(200), nullable=False)
    time = db.Column(db.String(200), nullable=False)
