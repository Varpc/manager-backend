# -*- coding: utf-8 -*-
from flask import Blueprint
import requests
from bs4 import BeautifulSoup
from manager.extensions import db
from manager.models import JiSuanKe, Codeforces, Root

crawler_bp = Blueprint('crawler', __name__)


@crawler_bp.route('/jisuanke', methods=['GET'])
def update_jisuanke():
    try:
        r = requests.get('https://nanti.jisuanke.com/contest')
    except:
        return '', r.status_code
    soup = BeautifulSoup(r.text, 'html.parser')

    tbody = soup.find("tbody", {"class": "jsk-text-light jsk-text-sm"})
    trs = tbody.find_all('tr', {'class': 'jsk-active'})

    old_data = JiSuanKe.query.all()
    for item in old_data:
        db.session.delete(item)
    db.session.commit()

    for item in trs:
        tds = item.find_all('td')
        ty = tds[0].string.strip()
        contest = tds[1].a.string.strip()
        url = tds[1].a.attrs.get('href')
        begin_time = tds[2].string.strip()
        time = tds[3].string.strip().replace(' ', '').replace('\n', '')
        jsk = JiSuanKe(type=ty, contest=contest, url=url, begin_time=begin_time, time=time)
        db.session.add(jsk)
    db.session.commit()

    return 'OK', r.status_code


@crawler_bp.route('/codeforces', methods=['GET'])
def update_codeforces():
    try:
        r = requests.get('http://codeforces.com/contests')
    except:
        return '', r.status_code
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find('table')
    trs = table.find_all('tr')[1:]

    old_data = Codeforces.query.all()
    for item in old_data:
        db.session.delete(item)
    db.session.commit()

    for tr in trs:
        tds = tr.find_all('td')
        contest = tds[0].string.strip()
        writer = tds[1].string.strip()
        begin_time = tds[2].span.string.strip()
        url = tds[2].a.attrs.get('href')
        time = tds[3].string.strip()
        codeforces = Codeforces(contest=contest, writer=writer, begin_time=begin_time, url=url, time=time)
        db.session.add(codeforces)
    db.session.commit()
    return 'OK', r.status_code
