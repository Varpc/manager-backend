# -*- coding: utf-8 -*-

from manager.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    class_ = db.Column(db.String(200))  # 加下划线与关键字不重复
    image = db.Column(db.String(200))
    username = db.Column(db.String(256))
    password_hash = db.Column(db.String(256))
    is_admin = db.Column(db.Boolean)
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
    name = db.Column(db.String(200))
    class_ = db.Column(db.String(200))
    count = db.Column(db.Integer)
    blue_book = db.Column(db.Integer)
    purple_book = db.Column(db.Integer)
    sum = db.Column(db.Integer)
    uva = db.Column(db.Integer)
    hdu = db.Column(db.Integer)
    poj = db.Column(db.Integer)
    cf = db.Column(db.Integer)
    bc = db.Column(db.Integer)
    status = db.Column(db.Integer)  # 0审核 1现役 2退役 3除名

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    no = db.Column(db.String(200), unique=True)
    member = db.relationship('User', back_populates='group')
