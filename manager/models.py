# -*- coding: utf-8 -*-

from manager.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    class_ = db.Column(db.String(200))  # 加下划线与关键字不重复
    username = db.Column(db.String(256), unique=True)
    password_hash = db.Column(db.String(256))
    is_admin = db.Column(db.Boolean)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

