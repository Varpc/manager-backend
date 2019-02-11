# -*- coding: utf-8 -*-

from manager.apis.resources import ProblemsApi, JisuankeApi, CodeforcesApi, BoardApi, GroupsApi, PostsApi, \
    EditerMediaApi, UpdateTimeIntervalApi

from manager.apis.admin import AdminPosts, AdminConfig, AdminHomeImageApi, AdminUsers, AdminGroups, AdminGroup

from manager.apis.user import UserPostApi, UserPostsApi, UserInfoApi, UserProblemApi, UserHeadImageApi, \
    UserAuthTokenApi, UserRegisterApi

from flask import Blueprint

apis = Blueprint('apis', __name__)

apis.add_url_rule('/problems', view_func=ProblemsApi.as_view('problems_api'), methods=['GET'])
apis.add_url_rule('/problem/<int:user_id>', view_func=UserProblemApi.as_view('problem_user_id_api'), methods=['GET'])

apis.add_url_rule('/auth', view_func=UserAuthTokenApi.as_view('auth_api'), methods=['POST', 'DELETE'])
apis.add_url_rule('/register', view_func=UserRegisterApi.as_view('register_api'), methods=['POST'])

apis.add_url_rule('/user/<int:user_id>', view_func=UserInfoApi.as_view('user_user_id_api'), methods=['GET', 'POST'])
apis.add_url_rule('/user/<int:user_id>/image', view_func=UserHeadImageApi.as_view('user_user_id_image_api'),
                  methods=['POST'])
apis.add_url_rule('/groups', view_func=GroupsApi.as_view('groups_api'), methods=['GET'])

apis.add_url_rule('/posts', view_func=PostsApi.as_view('posts_api'), methods=['GET'])  # 返回所有文章

# 对指定的文章进行操作: 获取指定文章 删除文章 修改文章
apis.add_url_rule('/post/<int:post_id>', view_func=UserPostApi.as_view('post_post_id_api'),
                  methods=['GET', 'DELETE', 'PUT'])
apis.add_url_rule('/post', view_func=UserPostApi.as_view('post_api'), methods=['POST'])  # 创建一个文章

apis.add_url_rule('/user/<int:user_id>/posts', view_func=UserPostsApi.as_view('user_user_id_posts_api'),
                  methods=['GET'])  # 返回一个用户的所有文章

apis.add_url_rule('/contest/jisuanke', view_func=JisuankeApi.as_view('contest_jisuanke_api'), methods=['GET'])
apis.add_url_rule('/contest/codeforces', view_func=CodeforcesApi.as_view('contest_codeforces_api'), methods=['GET'])

apis.add_url_rule('/admin/home/board', view_func=BoardApi.as_view('admin_home_board_api'), methods=['GET', 'POST'])
apis.add_url_rule('/admin/home/image', view_func=AdminHomeImageApi.as_view('admin_home_image_api'),
                  methods=['GET', 'POST', 'DELETE'])

apis.add_url_rule('/admin/users', view_func=AdminUsers.as_view('admin_users'), methods=['GET'])
apis.add_url_rule('/admin/group/<int:group_id>', view_func=AdminGroup.as_view('admin_group_group_id'),
                  methods=['PUT', 'DELETE'])
apis.add_url_rule('/admin/groups', view_func=AdminGroups.as_view('admin_groups'), methods=['GET', 'POST', 'PUT'])


apis.add_url_rule('/media', view_func=EditerMediaApi.as_view('media_api'), methods=['POST'])

apis.add_url_rule('/admin/crawler/time', view_func=UpdateTimeIntervalApi.as_view('admin_crawler_time_api'),
                  methods=['POST', 'GET'])
apis.add_url_rule('/admin/post/<int:post_id>', view_func=AdminPosts.as_view('admin_post_post_id_api'),
                  methods=['PUT', 'DELETE'])
apis.add_url_rule('/admin/config', view_func=AdminConfig.as_view('admin_config_api'), methods=['GET', 'PUT'])
