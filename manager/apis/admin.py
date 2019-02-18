# -*- coding: utf-8 -*-
import uuid, os
from flask import jsonify, request, current_app
from flask.views import MethodView
from manager.apis.error import api_abort
from manager.extensions import db
from manager.models import Post, Root, Image, Group, User, Problems, ContestSeason, Contest
from manager.apis.schemas import config_schema, group_schema, user_schema, contest_season_schema

"""
管理员后台的api
"""


class AdminPosts(MethodView):
    """管理员用于管理文章的api"""

    def put(self, post_id):
        """
        设置文章为需要修改
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
            image_url = current_app.config['IMAGE_UIR_PREFIX'] + filename
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


class AdminUsers(MethodView):
    def get(self):
        """获取所有的用户数据"""
        users = User.query.all()
        data = [user_schema(item) for item in users]
        return jsonify(data=data)


class AdminUser(MethodView):
    """用于审核用户，退役除名删除队员api"""
    def put(self, user_id):
        """
        改变用户id为user_id的用户状态，如审核->队员，队员->退役
        :param user_id:
        :return:
        """
        data = request.get_json()
        if data is None:
            return api_abort(400)
        status = data.get('status')
        if status is None:
            return api_abort(400)
        user = User.query.get_or_404(user_id)
        user.status = status
        db.session.commit()
        return api_abort(200)

    def delete(self, user_id):
        """
        删除用户id为user_id的用户
        :param user_id:
        :return:
        """
        user = User.query.get_or_404(user_id)
        problems = Problems.query.with_parent(user).first()
        posts = Post.query.with_parent(user).all()

        db.session.delete(user)
        db.session.delete(problems)
        for item in posts:
            db.session.delete(item)
        db.session.commit()
        return api_abort(200)


class AdminGroups(MethodView):
    def get(self):
        """
        返回所有的现役队伍的信息
        :return:
        """
        groups = Group.query.filter_by(service=True).all()
        data = [group_schema(item) for item in groups]
        return jsonify(data=data)

    def post(self):
        """
        创建一个新队伍，首先从请求中获取队伍名称（name），队伍编号（no）和队伍描述（describe 选填），若获取失败或或编号已经被战勇，
        则返回400错误，否则创建新队伍
        :return:
        """
        data = request.get_json()
        if not data:
            return api_abort(400)
        name = data.get('name')
        no = data.get('no')
        describe = data.get('describe')
        if not name or not no:
            return api_abort(400)
        if Group.query.filter_by(no=no).first() is not None:
            return api_abort(400, "编号已被占用")
        group = Group(name=name, no=no, describe=describe)
        db.session.add(group)
        db.session.commit()
        return api_abort(200)

    def put(self):
        """
        使所有队伍的分数清零
        :return:
        """
        groups = Group.query.filter_by(service=True).all()
        for item in groups:
            item.score = 0
        db.session.commit()
        return api_abort(200)


class AdminGroup(MethodView):
    def put(self, group_id):
        """
        修改队伍id为group_id的队伍的分数。从json中获取要改变的分数的大小（num）和修改的类型（type 类型为"plus"为加分，为"minus"
        则减分），若获取失败，返回400错误，否则修改相应的分数
        :param group_id: 队伍的id
        :return:
        """
        data = request.get_json()
        group = Group.query.get_or_404(group_id)
        if not data:
            return api_abort(400)
        type_ = data.get('type')
        num = data.get('num')
        if num is None or type_ is None:  # 此处不可使用not num，否则但num=0时会返回400
            return api_abort(400)
        if type_ == "plus":  # 这里不可用is加以判断
            group.score = group.score + num
        elif type_ == "minus":
            group.score = group.score - num
        db.session.commit()
        return api_abort(200)

    def delete(self, group_id):
        """
        删除id为group_id的队伍
        :return:
        """
        group = Group.query.get_or_404(group_id)
        db.session.delete(group)
        db.session.commit()
        return api_abort(200)


class AdminContestSeasonsApi(MethodView):
    def get(self):
        contest_season = ContestSeason.query.all()
        data = [contest_season_schema(item) for item in contest_season]
        return jsonify(data=data)

    def post(self):
        data = request.get_json()
        if data is None:
            return api_abort(400)
        name = data.get('name')
        begin_time = data.get('beginTime')
        end_time = data.get('endTime')
        rule = data.get('rule')
        if name is None or begin_time is None or end_time is None or rule is None:
            return api_abort(400)
        contest_season = ContestSeason(name=name, begin_time=begin_time, end_time=end_time, rule=rule)
        db.session.add(contest_season)
        db.session.commit()
        return api_abort(200)


class AdminContestSeasonApi(MethodView):
    def put(self, contest_season_id):
        data = request.get_json()
        contest_season = ContestSeason.query.get_or_404(contest_season_id)
        if data is None:
            return api_abort(400)
        name = data.get('name')
        begin_time = data.get('beginTime')
        end_time = data.get('endTime')
        rule = data.get('rule')
        if name is None or begin_time is None or end_time is None or rule is None:
            return api_abort(400)
        contest_season.name = name
        contest_season.begin_time = begin_time
        contest_season.end_time = end_time
        contest_season.rule = rule
        db.session.commit()
        return api_abort(200)

    def delete(self, contest_season_id):
        contest_season = ContestSeason.query.get_or_404(contest_season_id)
        contest = contest_season.contest
        for item in contest:
            db.session.delete(item)
        db.session.delete(contest_season)
        db.session.commit()
        return api_abort(200)


class AdminContestsApi(MethodView):
    def post(self):
        data = request.get_json()
        if data is None:
            return api_abort(200)
        saiji = data.get('saiji')
        name = data.get('name')
        type_ = data.get('type')
        problem_sum = data.get('problem')
        penalty = data.get('penalty')
        vj_data = data.get('data')
        date = data.get('date')
        time = data.get('time')
        length = data.get('length')

        try:
            contest = Contest(name=name,type=type_,problem_sum=problem_sum,penalty=penalty,
                              data=vj_data,date=date,time=time,length=length)
            contest_season = ContestSeason.query.get_or_404(saiji)
            contest.contest_season = contest_season
            db.session.add(contest)
            db.session.commit()
            return api_abort(200)
        except:
            db.session.rollback()
            return api_abort(400)


