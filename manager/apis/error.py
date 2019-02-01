# -*- coding: utf-8 -*-

from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def api_abort(code, message=None, **kwargs):
    """
    用于返回特定的http响应
    :param code: http响应的状态码
    :param message: 附加信息
    :param kwargs:
    :return: http响应
    """
    if message is None:
        message = HTTP_STATUS_CODES.get(code, '')

    response = jsonify(code=code, message=message, **kwargs)
    response.status_code = code
    return response
