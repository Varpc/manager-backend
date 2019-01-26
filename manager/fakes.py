# -*- coding: utf-8 -*-

from manager.extensions import db
from manager.models import User, Problems, Root, Post
from sqlalchemy.exc import IntegrityError
from faker import Faker
import random

fake = Faker(locale='zh_CN')
classes = ['计算机17-1', '计算机17-2', '计算机17-3', '计算机17-4', '计算机17-5', '软工17-1', '软工17-2', '网络17-1', '网络17-2', '物联网17-1',
           '物联网17-2']


def root_fake():
    root = Root()
    db.session.add(root)
    db.session.commit()


def user_fake():
    admin = User(name='admin', class_="计算机学院", username='username', is_admin=True)
    admin.set_password('password')
    problems = Problems()
    admin.problems = problems
    db.session.add(admin)
    db.session.add(problems)
    db.session.commit()

    length = len(classes)

    for i in range(80):
        name = fake.name()
        index = int(random.random() * length)
        class_ = classes[index]
        user = User(name=name, class_=class_, username=fake.user_name(), is_admin=False,
                    vjid=fake.user_name(), status=random.randint(0, 3))
        user.set_password('1234')

        problems = Problems(blue_book=random.randint(1, 100), purple_book=random.randint(100, 200),
                            uva=random.randint(100, 300), hdu=random.randint(1, 200), poj=random.randint(1, 200),
                            cf=random.randint(1000, 3000), bc=random.randint(1000, 3000), )
        problems.sum = problems.blue_book + problems.purple_book
        problems.count = problems.uva + problems.hdu + problems.poj
        problems.last_days = ""
        for i in range(0, 30):
            problems.last_days = problems.last_days + str(random.randint(0, 7)) + " "
        problems.last_days = problems.last_days.strip()
        try:
            user.problems = problems
            db.session.add(user)
            db.session.add(problems)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def post_fake():
    for i in range(50):
        post = Post(
            title=fake.sentence(),
            body=fake.text(2000),
            author=fake.name(),
            user=User.query.get(random.randint(1, User.query.count())),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(post)
    db.session.commit()
