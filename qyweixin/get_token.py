# -*- coding:utf-8 -*-

import contextlib
import urllib2

try:
    import json
except ImportError:
    import simplejson as json


class AccessToken(object):

    def __init__(self, corpid, corpsecret):
        self.corpid = corpid
        self.corpsecret = corpsecret

    def get_token(self):
        get_token_api = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + \
            self.corpid + '&corpsecret=' + self.corpsecret
        res = urllib2.Request(get_token_api)

        with contextlib.closing(urllib2.urlopen(res)) as r:
            resp = json.loads(r.read())

            if resp.get('access_token', None):
                return resp['access_token']
            else:
                print resp
                return
