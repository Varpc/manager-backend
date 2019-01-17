# -*- coding: utf-8 -*-

from manager.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class Root(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    board = db.Column(db.Text)  # 首页公告板内容
    # 另加各种更新的时间


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    class_ = db.Column(db.String(200), nullable=False)  # 加下划线与关键字不重复
    image = db.Column(db.String(200), default='/static/image/default.png')
    username = db.Column(db.String(256), nullable=False, index=True)
    password_hash = db.Column(db.String(256))
    is_admin = db.Column(db.Boolean, default=False)
    vjid = db.Column(db.String(200))

    # 外键
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    group = db.relationship('Group', back_populates='member')

    problems = db.relationship('Problems', uselist=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


class Problems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200),)
    class_ = db.Column(db.String(200))
    count = db.Column(db.Integer, default=0)
    blue_book = db.Column(db.Integer, default=0)
    purple_book = db.Column(db.Integer, default=0)
    sum = db.Column(db.Integer, default=0)
    uva = db.Column(db.Integer, default=0)
    hdu = db.Column(db.Integer, default=0)
    poj = db.Column(db.Integer, default=0)
    cf = db.Column(db.Integer, default=0)
    bc = db.Column(db.Integer, default=0)
    status = db.Column(db.Integer)  # 0审核 1现役 2退役 3除名

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')


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
