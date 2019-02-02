# -*- coding: utf-8 -*-

from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from manager.models import User


def generate_token(user):
    """
    为指定用户生成token
    :param user: User实例
    :return: token字符串，过期时间(单位：s)
    """
    expiration = 60 * 60 * 24
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    token = s.dumps({'id': user.id}).decode('ascii')
    return token, expiration


def validate_token(token):
    """
    解析token，并进行验证
    :param token: token字符串
    :return: token合法返回True,否则为False
    """
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except (BadSignature, SignatureExpired):
        return False
    user = User.query.get(data['id'])
    if user is None:
        return False
    g.current_user = user
    return True
