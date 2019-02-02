# -*- coding: utf-8 -*-

from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def api_abort(code, message=None, **kwargs):
    """
    用于返回特定的http响应
    :param code: http响应状态码
    :param message: 附加的在响应体中的消息
    :param kwargs: 其他响应体中的数据
    :return: http响应
    """
    if message is None:
        message = HTTP_STATUS_CODES.get(code, '')

    response = jsonify(code=code, message=message, **kwargs)
    response.status_code = code
    return response
