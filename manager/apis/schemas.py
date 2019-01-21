# -*- coding: utf-8 -*-
from manager.models import Problems, User, JiSuanKe, Codeforces, Post


def problems_schema(problems: Problems):
    return {
        'id': problems.id,
        'name': problems.name,
        'banji': problems.class_,
        'count': problems.count,
        'blue_book': problems.blue_book,
        'purple_book': problems.purple_book,
        'sum': problems.sum,
        'uva': problems.uva,
        'hdu': problems.hdu,
        'poj': problems.poj,
        'cf': problems.cf,
        'bc': problems.bc,
        'status': problems.status
    }


def user_schema(user: User):
    return {
        'id': user.id,
        'name': user.name,
        'banji': user.class_,
        'image': user.image,
        'username': user.username,
        'is_admin': user.is_admin,
        'vjid': user.vjid
    }


# 为提高加载速度，文章内容通过need_body按需提供
def post_schema(post: Post, need_body=True):
    item = {
        'post_id': post.id,
        'user_id': post.user_id,
        'title': post.title,
        'author': post.author,
        'time': post.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
    }
    if need_body:
        item['body'] = post.body
    return item


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
