# -*- coding: utf-8 -*-
import uuid, os
from flask import jsonify, request, current_app
from flask.views import MethodView
from manager.apis.error import api_abort
from manager.extensions import db
from manager.models import Post, Root, Image
from manager.apis.schemas import config_schema

"""
管理员后台的api
"""


class AdminPosts(MethodView):
    """管理员用于管理文章的api"""

    def put(self, post_id):
        """
        设置文章需要修改
        :param post_id: 文章id
        :return:
        """
        post = Post.query.get_or_404(post_id)
        post.need_edit = True
        db.session.commit()
        return api_abort(200)

    def delete(self, post_id):
        """
        删除文章
        :param post_id: 文章id
        :return:
        """
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return api_abort(200)


class AdminConfig(MethodView):
    """管理员用于网站的基本设置api"""
    def get(self):
        """获取基本配置"""
        root = Root.query.first()
        return jsonify(config_schema(root))

    def put(self):
        """更新配置"""
        data = request.get_json()
        if data is None:
            return api_abort(400)

        jisuanke_update_interval = data.get('jisuanke_update_interval')
        codeforces_update_interval = data.get('codeforces_update_interval')
        wait_tiem = data.get('wait_time')
        try_time = data.get('try_time')

        if not jisuanke_update_interval or not codeforces_update_interval or not wait_tiem \
            or not try_time:
            return api_abort(400)
        root = Root.query.first()
        root.jisuanke_update_interval = jisuanke_update_interval
        root.codeforces_update_interval = codeforces_update_interval
        root.wait_time = wait_tiem
        root.try_time = try_time
        db.session.commit()
        return api_abort(200)


class AdminHomeImageApi(MethodView):
    """用于操作首页轮播图片的api"""
    def get(self):
        """获取首页图片"""
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
