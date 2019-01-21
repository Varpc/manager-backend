# -*- coding: utf-8 -*-
from flask import Blueprint

apis = Blueprint('apis', __name__)

from manager.apis.resources import ProblemsApi, AuthTokenApi, RegisterApi, JisuankeApi, CodeforcesApi, BoardApi, \
    EditerMediaApi, HomeImageApi, UpdateTimeIntervalApi, PostApi, PostsApi, UserPostApi

apis.add_url_rule('/problems', view_func=ProblemsApi.as_view('problems_api'), methods=['GET'])
apis.add_url_rule('/auth', view_func=AuthTokenApi.as_view('auth_api'), methods=['POST', 'DELETE'])
apis.add_url_rule('/register', view_func=RegisterApi.as_view('register_api'), methods=['POST'])

apis.add_url_rule('/posts', view_func=PostsApi.as_view('posts_api'), methods=['GET'])  # 返回所有文章
apis.add_url_rule('/post/<int:id>', view_func=PostApi.as_view('post_api'), methods=['GET', 'DELETE'])  # 返回指定的文章
apis.add_url_rule('/post', view_func=PostApi.as_view('post_create_api'), methods=['POST'])  # 创建一个文章
apis.add_url_rule('/user/<int:id>/posts', view_func=UserPostApi.as_view('user_posts_apo'), methods=['GET'])  # 返回一个用
# 户的所有文章

apis.add_url_rule('/contest/jisuanke', view_func=JisuankeApi.as_view('jisuanke_api'), methods=['GET'])
apis.add_url_rule('/contest/codeforces', view_func=CodeforcesApi.as_view('codeforces_api'), methods=['GET'])

apis.add_url_rule('/admin/home/board', view_func=BoardApi.as_view('board_api'), methods=['GET', 'POST'])
apis.add_url_rule('/admin/home/image', view_func=HomeImageApi.as_view('home_image_api'), methods=['GET', 'POST',
                                                                                                  'DELETE'])

apis.add_url_rule('/media', view_func=EditerMediaApi.as_view('media_api'), methods=['POST'])

apis.add_url_rule('/admin/crawler/time', view_func=UpdateTimeIntervalApi.as_view('crawler_time_api'), methods=['POST',
                                                                                                               'GET'])
