# -*- coding: utf-8 -*-
from flask import Blueprint

apis = Blueprint('apis', __name__)

from manager.apis.resources import ProblemsApi, AuthTokenApi

apis.add_url_rule('/problems', view_func=ProblemsApi.as_view('problems_api'), methods=['GET'])
apis.add_url_rule('/auth', view_func=AuthTokenApi.as_view('auth_api'), methods=['POST', 'DELETE'])
