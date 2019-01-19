# -*- coding: utf-8 -*-

import uuid, os
from flask import jsonify, request, current_app
from flask.views import MethodView

from manager.apis.schemas import problems_schema, user_schema, jisuanke_schema, codeforces_schema
from manager.apis.error import api_abort
from manager.apis.auth import generate_token, validate_token
from manager.extensions import db
from manager.models import User, Problems, JiSuanKe, Codeforces, Root


class ProblemsApi(MethodView):
    def get(self):
        problems = Problems.query.all()
        data = []
        for item in problems:
            data.append(problems_schema(item))
        return jsonify(data=data)


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


# 近期比赛api
class JisuankeApi(MethodView):
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

