# -*- coding: utf-8 -*-
from flask import url_for
from manager.models import Problems, User


def problems_schema(problems: Problems):
    return {
        'id': problems.id,
        'name': problems.name,
        'banji': problems.class_,
        'count': problems.count,
        'blue_book': problems.blue_book,
        'purple_book': problems.purple_book,
        'sum': problems.sum,
        'uva': problems.uva,
        'hdu': problems.hdu,
        'poj': problems.poj,
        'cf': problems.cf,
        'bc': problems.bc,
        'status': problems.status
    }


def user_schema(user: User):
    return {
        'id': user.id,
        'name': user.name,
        'banji': user.class_,
        'image': user.image,
        'username': user.username,
        'is_admin': user.is_admin,
        'vjid': user.vjid
    }
