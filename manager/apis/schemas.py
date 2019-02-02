# -*- coding: utf-8 -*-
from manager.models import Problems, User, JiSuanKe, Codeforces, Post, Group, Root

"""
用于格式化数据的工具函数
"""


# 为提高加载速度, 指定need_last_days，最近三十天记录按需提供
def problems_schema(problems: Problems, need_last_days=False):
    user = problems.user
    item = {
        'id': problems.id,
        'count': problems.count,
        'blue_book': problems.blue_book,
        'purple_book': problems.purple_book,
        'sum': problems.sum,
        'uva': problems.uva,
        'hdu': problems.hdu,
        'poj': problems.poj,
        'cf': problems.cf,
        'bc': problems.bc,
        'user': {
            'user_id': user.id,
            'name': user.name,
            'banji': user.class_,
            'status': user.status,
        }
    }

    if need_last_days:
        last_days = problems.last_days.split(' ')
        last_days_data = []
        for i in last_days:
            last_days_data.append(eval(i))
        item['last_days'] = last_days_data

    return item


def user_schema(user: User):
    return {
        'id': user.id,
        'name': user.name,
        'banji': user.class_,
        'image': user.image,
        'username': user.username,
        'is_admin': user.is_admin,
        'vjid': user.vjid,
        'codeforces': user.codeforces,
        'status': user.status,
        'blog': user.blog
    }


def group_schema(group: Group):
    user = []
    for item in group.member:
        user.append(user_schema(item))

    return {
        'group_id': group.id,
        'name': group.name,
        'no': group.no,
        'score': group.score,
        'user': user,
    }


# 为提高加载速度，文章内容通过need_body按需提供
def post_schema(post: Post, need_body=True):
    item = {
        'post_id': post.id,
        'user_id': post.user_id,
        'title': post.title,
        'author': post.author,
        'need_edit': post.need_edit,
        'time': post.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
    }
    if need_body:
        item['body'] = post.body
    return item


# 用于格式化root中的设置
def config_schema(root: Root):
    return {
        'jisuanke_update_interval': root.jisuanke_update_interval,
        'codeforces_update_interval': root.codeforces_update_interval,
        'wait_time': root.wait_time,
        'try_time': root.try_time,
    }


# 格式化近期比赛数据
def jisuanke_schema(jsk: JiSuanKe):
    return {
        'id': jsk.id,
        'type': jsk.type,
        'contest': jsk.contest,
        'url': jsk.url,
        'begin_time': jsk.begin_time,
        'time': jsk.time
    }


def codeforces_schema(cf: Codeforces):
    return {
        'id': cf.id,
        'contest': cf.contest,
        'url': cf.url,
        'writer': cf.writer,
        'begin_time': cf.begin_time,
        'time': cf.time
    }
