# -*- coding: utf-8 -*-

import uuid, os
from crawler_manager import change_update_callback

from flask import jsonify, request, current_app
from flask.views import MethodView

from manager.apis.schemas import problems_schema, user_schema, jisuanke_schema, codeforces_schema, post_schema
from manager.apis.error import api_abort
from manager.apis.auth import generate_token, validate_token
from manager.extensions import db
from manager.models import User, Problems, JiSuanKe, Codeforces, Root, Image, Post


class ProblemsApi(MethodView):
    def get(self):
        problems = Problems.query.all()
        data = []
        for item in problems:
            data.append(problems_schema(item))
        return jsonify(data=data)


# 返回指定用户的题目列表
class ProblemApi(MethodView):
    def get(self, user_id):
        problem = User.query.get_or_404(user_id).problems
        return jsonify(problems_schema(problem, need_last_days=True))


# 返回某个特定用于的信息，用户信息修改
class UserApi(MethodView):
    def get(self, id):
        user = User.query.get_or_404(id)
        return jsonify(user_schema(user))

    def post(self, id):
        user = User.query.get_or_404(id)
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


# 用户头像修改api
class HeadImageApi(MethodView):
    def post(self, id):
        file = request.files['file']
        if file:
            # 获取新头像
            filename = str(uuid.uuid1()) + file.filename
            filepath = os.path.join(current_app.config['IMAGE_DIR'], filename)
            file.save(filepath)
            image_url = current_app.config['IMAGE_DIR_SUFFIX'] + filename

            user = User.query.get_or_404(id)
            if user.image != current_app.config['DEFAULT_HEAD_IMAGE_URI']:
                old_filename = user.image.split('/')[-1:][0]
                os.chdir(current_app.config['IMAGE_DIR'])
                if os.path.exists(old_filename):
                    os.remove(old_filename)

            user.image = image_url
            db.session.commit()
            return jsonify(code="0", imgURL=image_url, downloadURL=image_url)
        return api_abort(400)


class AuthTokenApi(MethodView):
    def post(self):
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
        return api_abort(200, '登出成功')


class RegisterApi(MethodView):
    def post(self):
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


# 用于文章的api

# 返回所有文章
class PostsApi(MethodView):
    def get(self):
        posts = Post.query.order_by(Post.timestamp.desc()).all()
        data = []
        for item in posts:
            data.append(post_schema(item, need_body=False))
        return jsonify(data=data)


# 返回指定文章和创建删除文章
class PostApi(MethodView):
    def get(self, id):
        post = Post.query.get_or_404(id)
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

    def delete(self, id):
        post = Post.query.get_or_404(id)
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


# 首页公告提交
class BoardApi(MethodView):
    def get(self):
        root = Root.query.first()
        return jsonify(html=root.board)

    def post(self):
        data = request.get_json()
        if data is None:
            return api_abort(400, '提交失败')
        html = data.get('html')
        if html is None:
            return api_abort(400, '提交失败')
        root = Root.query.first()
        root.board = html
        db.session.commit()
        return api_abort(200, '提交成功')


# 富文本编辑器的媒体文件提交api
class EditerMediaApi(MethodView):
    def post(self):
        file = request.files['file']
        if file:
            filename = str(uuid.uuid1()) + file.filename
            filepath = os.path.join(current_app.config['IMAGE_DIR'], filename)
            file.save(filepath)
            return current_app.config['IMAGE_DIR_SUFFIX'] + filename, 200
        return api_abort(400)


# 用于接收首页图片的修改提交
class HomeImageApi(MethodView):
    def get(self):
        root = Root.query.first()
        images = Image.query.with_parent(root).all()
        image_list = []
        for item in images:
            filename = item.url.split('/')[-1:][0]
            image_list.append(dict(imgURL=item.url, name=filename))
        return jsonify(data=image_list)

    def post(self):
        file = request.files['file']
        if file:
            filename = str(uuid.uuid1()) + file.filename
            filepath = os.path.join(current_app.config['IMAGE_DIR'], filename)
            file.save(filepath)
            image_url = current_app.config['IMAGE_DIR_SUFFIX'] + filename
            root = Root.query.first()
            image = Image(url=image_url)
            root.image.append(image)
            db.session.add(image)
            db.session.commit()
            return jsonify(code="0", imgURL=image_url, downloadURL=image_url)
        return api_abort(400)

    def delete(self):
        data = request.get_json()
        if data is None:
            return api_abort(400)
        image_url = data.get('imgURL')
        if image_url is None:
            return api_abort(400)
        filename = image_url.split('/')[-1:][0]
        filepath = current_app.config['IMAGE_DIR']
        os.chdir(filepath)
        if os.path.exists(filename):
            os.remove(filename)
        image = Image.query.filter_by(url=image_url).first()
        if image is not None:
            db.session.delete(image)
            db.session.commit()
        return api_abort(200)


# 近期比赛api
class JisuankeApi(MethodView):  # noqa
    def get(self):
        jsk = JiSuanKe.query.all()
        data = []
        for item in jsk:
            data.append(jisuanke_schema(item))
        root = Root.query.first()
        if root is not None:
            time = root.jisuanke_update_time.strftime('%Y-%m-%d %H:%M:%S')
        return jsonify(data=data, time=time)


class CodeforcesApi(MethodView):
    def get(self):
        codeforces = Codeforces.query.all()
        data = []
        for item in codeforces:
            data.append(codeforces_schema(item))
        root = Root.query.first()
        if root is not None:
            time = root.codeforces_update_time.strftime('%Y-%m-%d %H:%M:%S')
        return jsonify(data=data, time=time)


class UpdateTimeIntervalApi(MethodView):
    def get(self):
        root = Root.query.first()
        change_update_callback(jisuanke=root.jisuanke_update_interval, codeforces=root.codeforces_update_interval,
                               vjudge=root.vjudge_update_interval, wait_time=root.wait_time, try_time=root.try_time)
        return jsonify(jisuanke=root.jisuanke_update_interval, codeforces=root.codeforces_update_interval,
                               vjudge=root.vjudge_update_interval, wait_time=root.wait_time, try_time=root.try_time)

    def post(self):
        data = request.get_json()
        if data is None:
            return api_abort(400)
        jisuanke_interval = data.get('jisuanke')
        codeforces_interval = data.get('codeforces')
        vjudge_interval = data.get('vjudge')
        wait_time = data.get('wait_time')
        try_time = data.get('try_time')
        if not jisuanke_interval or not codeforces_interval or not vjudge_interval or not wait_time or not try_time:
            return api_abort(400)
        root = Root.query.first()
        root.jisuanke_update_interval = jisuanke_interval
        root.codeforces_update_interval = codeforces_interval
        root.vjudge_update_interval = vjudge_interval
        root.wait_time = wait_time
        root.try_time = try_time
        db.session.commit()
        change_update_callback(jisuanke=jisuanke_interval, codeforces=codeforces_interval, vjudge=vjudge_interval,
                               wait_time=wait_time, try_time=try_time)
        return 'OK', 200
