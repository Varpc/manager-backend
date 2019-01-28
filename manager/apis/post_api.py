# -*- coding: utf-8 -*-

from flask import jsonify, request, current_app
from flask.views import MethodView
from manager.apis.error import api_abort
from manager.apis.schemas import post_schema
from manager.models import Post, User
from manager.extensions import db
from datetime import datetime

"""
用于文章的api
"""


# 返回所有文章
class PostsApi(MethodView):
    def get(self):
        posts = Post.query.order_by(Post.timestamp.desc()).all()
        data = []
        for item in posts:
            data.append(post_schema(item, need_body=False))
        return jsonify(data=data)


class PostApi(MethodView):
    """
    对一个进行操作的api，post方法用于创建一个文章
    除post方法外，其他三个方法需通过post_id来指定所要
    操作的文章的id,分别对文章进行获取，修改，删除操作
    """
    def get(self, post_id):
        post = Post.query.get_or_404(post_id)
        return jsonify(post_schema(post))

    def post(self):
        data = request.get_json()
        title = data.get('title')
        body = data.get('body')
        author = data.get('author')
        user_id = data.get('user_id')
        if not title or not body or not author or not user_id:
            return api_abort(400)
        user = User.query.get_or_404(user_id)
        post = Post(title=title, body=body, author=author)
        post.user = user
        db.session.add(post)
        db.session.commit()
        return api_abort(200)

    def put(self, post_id):
        data = request.get_json()
        title = data.get('title')
        body = data.get('body')
        author = data.get('author')
        user_id = data.get('user_id')
        if not title or not body or not author or not user_id:
            return api_abort(400)
        post = Post.query.get_or_404(post_id)
        post.title = title
        post.body = body
        post.author = author
        post.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        post.need_edit = False
        db.session.commit()
        return api_abort(200)

    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return api_abort(200)


# 返回指定用户的文章
class UserPostApi(MethodView):
    def get(self, id):
        user = User.query.get_or_404(id)
        posts = Post.query.with_parent(user).order_by(Post.timestamp.desc()).all()
        data = []
        for item in posts:
            data.append(post_schema(item, need_body=False))
        return jsonify(data=data)
