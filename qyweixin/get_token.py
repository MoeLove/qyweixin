# -*- coding:utf-8 -*-

import contextlib
import urllib2

try:
    import json
except ImportError:
    import simplejson as json


class AccessToken(object):

    def __init__(self, corpid, corpsecret):
        self._corpid = corpid
        self._corpsecret = corpsecret

    def get_token(self):
        get_token_api = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (
            self._corpid, self._corpsecret)
        res = urllib2.Request(get_token_api)

        try:
            with contextlib.closing(urllib2.urlopen(res)) as r:
                resp = json.loads(r.read())

                if resp.get('access_token', None):
                    return resp['access_token']
                else:
                    return False
        except:
            return False
