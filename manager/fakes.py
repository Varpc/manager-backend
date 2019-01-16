# -*- coding: utf-8 -*-

from manager.extensions import db
from manager.models import User, Problems, Group
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
        name = fake.name()
        index = int(random.random() * length)
        class_ = classes[index]
        image = 'E:\manager-backend\image\1.jpeg'

        user = User(name=name, class_=class_, image=image, username=fake.user_name(), is_admin=False,
                    vjid=fake.user_name())
        user.set_password('1234')

        problems = Problems(name=name, class_=class_, count=fake.random_int(), blue_book=fake.random_int(),
                            purple_book=fake.random_int(), sum=fake.random_int(), uva=fake.random_int(),
                            hdu=fake.random_int(), poj=fake.random_int(), cf=fake.random_int(), bc=fake.random_int(),
                            status=int(random.random() * 4))
        try:
            user.problems = problems
            db.session.add(user)
            db.session.add(problems)
        except:
            db.session.rollback()
