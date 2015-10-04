# -*- coding:utf-8 -*-

import json

import requests


def upload(token, img_name, img_path):

    url = 'https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=image' % token
    multi_files = [('media', (img_name, open(img_path, 'rb'), 'image/jpeg'))]
    res = requests.post(url, files=multi_files)

    if json.loads(res.content).get('media_id', None):
        return True
    else:
        return False
