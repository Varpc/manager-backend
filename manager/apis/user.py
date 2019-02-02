# -*- coding: utf-8 -*-
import uuid, os
from flask import jsonify, request, current_app
from flask.views import MethodView
from manager.apis.error import api_abort
from manager.apis.schemas import post_schema, problems_schema, user_schema
from manager.apis.auth import generate_token
from manager.models import Post, User
from manager.extensions import db
from datetime import datetime


"""
用于用户操作的api，全部以User-为前缀加以取区分
"""


class UserPostsApi(MethodView):
    """用于操作指定用户所有文章的api"""
    def get(self, user_id):
        """
        返回指定用户的文章
        :param user_id: 用户id
        :return: http响应，json格式
        """
        user = User.query.get_or_404(user_id)
        posts = Post.query.with_parent(user).order_by(Post.timestamp.desc()).all()
        data = []
        for item in posts:
            data.append(post_schema(item, need_body=False))
        return jsonify(data=data)


class UserPostApi(MethodView):
    """
    对一个文章进行操作的api，只通过json格式进行交互，post方法用于创建一个文章。除post方法外，其他三个方法需通过post_id来指定所要
    操作的文章的id,分别对文章进行获取，修改，删除操作
    """

    def get(self, post_id):
        """
        返回指定的文章
        :param post_id: 文章的id
        :return: 文章数据，json格式
        """
        post = Post.query.get_or_404(post_id)
        return jsonify(post_schema(post))

    def post(self):
        """
        创建一个文章，首先获取json数据中的文章标题，文章内容，作者和作者的id，若获取失败则返回400响应，成功则新创建文章，其中文章的
        时间为当前的时间（由数据库中的default指定）
        :return: 200响应(创建成功) or 400响应(创建失败)
        """
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
        """
        对指定文章进行修改（类似post方法），并更新文章的创建时间
        :param post_id: 文章的id
        :return: 200响应(修改成功) or 400响应(修改失败)
        """
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
        """
        删除指定文章
        :param post_id: 文章的id
        :return: 200响应(删除成功) or 400响应(删除失败)
        """
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return api_abort(200)


class UserProblemApi(MethodView):
    """用于操作指定用户的刷题信息的api"""
    def get(self, user_id):
        """
        返回指定用户的刷题统计信息
        :param user_id: 用户的id
        :return: 用户的刷题信息，json格式
        """
        problem = User.query.get_or_404(user_id).problems
        return jsonify(problems_schema(problem, need_last_days=True))


class UserInfoApi(MethodView):
    """用于操作指定用户信息的api"""
    def get(self, user_id):
        """
        获取指定用户的信息
        :param user_id:
        :return:
        """
        user = User.query.get_or_404(user_id)
        return jsonify(user_schema(user))

    def post(self, user_id):
        """
        修改指定用户的信息
        :param user_id:
        :return:
        """
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        name = data.get('name')
        class_ = data.get('banji')
        vjid = data.get('vjid')
        if name is None or class_ is None or vjid is None:
            return api_abort(400)
        user.name = name
        user.class_ = class_
        user.vjid = vjid
        if data.get('blog'):
            user.blog = data.get('blog')
        if data.get('codeforces'):
            user.codeforces = data.get('codeforces')
        if data.get('password'):
            user.set_password(data.get('password'))

        db.session.commit()
        return api_abort(200)


class UserHeadImageApi(MethodView):
    """用于修改用户头像的api"""
    def post(self, user_id):
        """
        修改用户头像，该api需使用multipart/form-data格式进行请求，并将头像所在的字段设置为'file'。获取头像后，会为头像生成一个全
        局唯一的文件名后保存到指定文件夹。若用户的旧头像不是默认的头像，则进行删除，否则，则不删除，并更新数据库
        :param user_id: 用户id
        :return: 400响应（修改失败），图片URI(修改成功)
        """
        file = request.files['file']
        if file:
            filename = str(uuid.uuid1()) + file.filename
            filepath = os.path.join(current_app.config['IMAGE_DIR'], filename)
            file.save(filepath)
            image_url = current_app.config['IMAGE_DIR_SUFFIX'] + filename

            user = User.query.get_or_404(user_id)
            if user.image != current_app.config['DEFAULT_HEAD_IMAGE_URI']:
                old_filename = user.image.split('/')[-1:][0]
                os.chdir(current_app.config['IMAGE_DIR'])
                if os.path.exists(old_filename):
                    os.remove(old_filename)

            user.image = image_url
            db.session.commit()
            return jsonify(code="200", imgURL=image_url, downloadURL=image_url)
        return api_abort(400)


class UserAuthTokenApi(MethodView):
    """用于用户登陆和登出的api"""
    def post(self):
        """
        用于用户登陆的api，通过json格式的请求体获取用户名和密码，返回用户的信息和token以及token的过期时间
        :return: 400响应（登陆失败）， 用户信息和token（登陆成功）
        """
        data = request.get_json()
        if not data:
            return api_abort(400, '无效的用户名或密码')
        username = data.get('username')
        password = data.get('password')
        if username is None or password is None:
            return api_abort(400, '无效的用户名和密码')

        user = User.query.filter_by(username=username).first()
        if user is None or not user.validate_password(password):
            return api_abort(400, '用户名或密码错误')

        token, expiration = generate_token(user)

        response_data = user_schema(user)
        response_data['token'] = token
        response_data['expiration'] = expiration
        response = jsonify(response_data)
        response.headers['Cache-Control'] = 'no-store'
        response.headers['Pragma'] = 'no-cache'
        return response

    def delete(self):
        """用于用户的登出"""
        return api_abort(200, '登出成功')


class UserRegisterApi(MethodView):
    """用于用户注册的api"""
    def post(self):
        """
        创建新用户
        :return: 用户的信息
        """
        data = request.get_json()
        if data is None:
            return api_abort(400, '无效的数据')
        username = data.get('username')
        password = data.get('password')
        class_ = data.get('class_')
        name = data.get('name')
        if username is None or password is None or class_ is None or name is None:
            return api_abort(400, '无效的数据')

        if User.query.filter_by(username=username).first() is not None:
            return api_abort(400, '用户名已被占用')

        user = User(username=username, name=name, class_=class_, is_admin=False, image='/static/image/1.jpeg')
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        return jsonify(user_schema(user))
