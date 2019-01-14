# -*- coding: utf-8 -*-

from manager.extensions import db
from manager.models import User
from faker import Faker
import random

fake = Faker(locale='zh_CN')
classes = ['计算机17-1', '计算机17-2', '计算机17-3', '计算机17-4', '计算机17-5', '软工17-1', '软工17-2', '网络17-1', '网络17-2', '物联网17-1',
           '物联网17-2']


def fakes():
    db.drop_all()
    db.create_all()
    user_fake()


def user_fake():
    admin = User(name='admin', class_="计算机学院", username='username', is_admin=True)
    admin.set_password('password')

    db.session.add(admin)
    db.session.commit()

    length = len(classes)

    for i in range(80):
        index = int(random.random() * length)
        user = User(name=fake.name(), class_=classes[index], username=fake.user_name(), is_admin=False)
        user.set_password('12345')
        try:
            db.session.add(user)
            db.session.commit()
        except:
            pass
