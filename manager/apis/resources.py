# -*- coding: utf-8 -*-

from flask import jsonify, request
from flask.views import MethodView

from manager.apis.schemas import problems_schema, user_schema
from manager.apis.error import api_abort
from manager.apis.auth import generate_token, validate_token
from manager.extensions import db
from manager.models import User, Problems


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
