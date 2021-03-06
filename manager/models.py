# -*- coding: utf-8 -*-

from manager.extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from manager.settings import BaseConfig


# 基本配置表
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


# 首页图片表
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256), default=BaseConfig.DEFAULT_HOME_IMAGE_URI)
    root_id = db.Column(db.Integer, db.ForeignKey('root.id'))
    root = db.relationship('Root', back_populates='image')


# 用户信息表
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    class_ = db.Column(db.String(200), nullable=False)  # 加下划线与关键字不重复
    image = db.Column(db.String(256), default=BaseConfig.DEFAULT_HEAD_IMAGE_URI)
    username = db.Column(db.String(256), nullable=False, unique=True)
    status = db.Column(db.Integer, default=0)  # 0审核 1现役 2退役 3除名
    password_hash = db.Column(db.String(256))
    is_admin = db.Column(db.Boolean, default=False)
    vjid = db.Column(db.String(200))
    codeforces = db.Column(db.String(200))
    blog = db.Column(db.String(256))

    # 外键
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    group = db.relationship('Group', back_populates='member')
    #
    problems = db.relationship('Problems', back_populates='user', uselist=False)
    post = db.relationship('Post', back_populates='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


# 文章表
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.now)
    need_edit = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='post')


# 刷题统计表
class Problems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)
    blue_book = db.Column(db.Integer, default=0)
    purple_book = db.Column(db.Integer, default=0)
    sum = db.Column(db.Integer, default=0)
    uva = db.Column(db.Integer, default=0)
    hdu = db.Column(db.Integer, default=0)
    poj = db.Column(db.Integer, default=0)
    cf = db.Column(db.Integer, default=0)
    bc = db.Column(db.Integer, default=0)
    last_days = db.Column(db.String(1000), default=('0 ' * 30).strip())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='problems')


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    no = db.Column(db.String(200), unique=True, index=True)
    score = db.Column(db.Float, default=0.0)
    describe = db.Column(db.Text)
    service = db.Column(db.Boolean, default=False)
    member = db.relationship('User', back_populates='group')


class ContestSeason(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    begin_time = db.Column(db.BigInteger, nullable=False)
    end_time = db.Column(db.BigInteger, nullable=False)
    rule = db.Column(db.Text)
    creator = db.Column(db.String(200), nullable=False, default='admin')
    contest = db.relationship('Contest', back_populates='contest_season')


class Contest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    type = db.Column(db.Integer, nullable=False)  # 0 为个人赛， 1为组队赛
    problem_sum = db.Column(db.Integer, nullable=False)  # 题目数量
    penalty = db.Column(db.Integer, nullable=False)  # 每道题罚时，单位分钟
    data = db.Column(db.Text, nullable=False)  # vj上的榜单数据
    date = db.Column(db.BigInteger, nullable=False)  # 比赛日期，和GMT时间1970年1月1日之间相差的毫秒数
    time = db.Column(db.BigInteger, nullable=False)  # 比赛时间，在一天中的第几秒
    length = db.Column(db.Integer, nullable=False)  # 比赛时长,以秒为单位
    creator = db.Column(db.String(200), default='admin')  # 创建者

    contest_season_id = db.Column(db.Integer, db.ForeignKey('contest_season.id'))
    contest_season = db.relationship('ContestSeason', back_populates='contest')


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
