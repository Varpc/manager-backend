# -*- coding: utf-8 -*-

import uuid, os
from crawler_manager import change_update_callback

from flask import jsonify, request, current_app
from flask.views import MethodView

from manager.apis.schemas import problems_schema, jisuanke_schema, codeforces_schema, post_schema, group_schema
from manager.apis.error import api_abort
from manager.extensions import db
from manager.models import Problems, JiSuanKe, Codeforces, Root, Group, Post


"""
这里包括大多数公有资源的api
"""


class ProblemsApi(MethodView):
    """用于获取所有刷题记录的api"""

    def get(self):
        problems = Problems.query.all()
        data = [problems_schema(item) for item in problems]
        return jsonify(data=data)


class PostsApi(MethodView):
    """用于获取所有文章的api"""

    def get(self):
        posts = Post.query.order_by(Post.timestamp.desc()).all()
        data = [post_schema(item, need_body=False) for item in posts]
        return jsonify(data=data)


class GroupsApi(MethodView):
    """用于获取所有队伍信息的api"""

    def get(self):
        groups = Group.query.order_by(Group.score.desc()).all()
        data = [group_schema(item) for item in groups]
        return jsonify(data=data)


class BoardApi(MethodView):
    """用于首页公告操作的api"""

    def get(self):
        """获取首页公告"""
        root = Root.query.first()
        return jsonify(html=root.board)

    def post(self):
        """修改首页公告"""
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


class EditerMediaApi(MethodView):
    """富文本编辑器的媒体文件的api"""

    def post(self):
        """
        提交媒体文件的api，包括图片，视频，音乐，该api需使用multipart/form-data格式进行请求，并将媒体文件的字段名设置为'file',
        接受成功后，会为文件生成一个全局唯一的字符串，并将原文件名附加到后面保存到指定文件夹
        :return: 400响应（接受成功）， 媒体文件URI（接受成功）
        """
        file = request.files['file']
        if file:
            filename = str(uuid.uuid1()) + file.filename
            filepath = os.path.join(current_app.config['IMAGE_DIR'], filename)
            file.save(filepath)
            return current_app.config['IMAGE_DIR_SUFFIX'] + filename, 200
        return api_abort(400)


class JisuankeApi(MethodView):
    """获取计蒜客近期比赛的api"""

    def get(self):
        jsk = JiSuanKe.query.all()
        data = [jisuanke_schema(item) for item in jsk]
        root = Root.query.first()
        time = root.jisuanke_update_time.strftime('%Y-%m-%d %H:%M:%S')
        return jsonify(data=data, time=time)


class CodeforcesApi(MethodView):
    """获取codeforces近期比赛的api"""

    def get(self):
        codeforces = Codeforces.query.all()
        data = [codeforces_schema(item) for item in codeforces]
        root = Root.query.first()
        time = root.codeforces_update_time.strftime('%Y-%m-%d %H:%M:%S')
        return jsonify(data=data, time=time)


class UpdateTimeIntervalApi(MethodView):
    """"""

    def get(self):
        """
        此接口只供控制爬虫控制进程调用
        用于获取root爬虫控制进程中的基本配置，change_update_callback函数用于改变爬虫控制进程中运行时的全局配置
        :return: 控制进程基本配置，json格式
        """
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
