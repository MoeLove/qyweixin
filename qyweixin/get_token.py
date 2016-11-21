# -*- coding:utf-8 -*-

import contextlib
import urllib2

try:
    import json
except ImportError:
    import simplejson as json


class AccessToken(object):

    def get_token(self, corpid, corpsecret):
        get_token_api = ('https://qyapi.weixin.qq.com/cgi-bin/gettoken?'
                         'corpid={corpid}&corpsecret={corpsecret}').format(
                corpid=corpid, corpsecret=corpsecret)
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


def get_token(corpid, corpsecret):
    """
    Please use your corpid and corpsecret for get token.
    """
    qy = AccessToken()
    return qy.get_token(corpid, corpsecret)
