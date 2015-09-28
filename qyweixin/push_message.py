# -*- coding:utf-8 -*-

import contextlib
import urllib2

from config import AGENTID, CORPID, CORPSECRET

try:
    import json
except ImportError:
    import simplejson as json


class WeixinPush(object):

    def __init__(self, corpid, corpsecret):
        self.corpid = corpid
        self.corpsecret = corpsecret

    def _target_format(self, target):
        if isinstance(target, list):
            return '|'.join(target)
        else:
            return target

    def push_text_message(self, token=None, agentid=AGENTID, content='',
                          touser='@all', toparty='', totag='', **kwargs):
        message_body = {
            'touser': self._target_format(touser),
            'toparty': self._target_format(toparty),
            'totag': self._target_format(totag),
            'msgtype': 'text',
            'text': {
                'content': content
            },
            'agentid': agentid,
            'safe': kwargs.get('safe', 0)
        }

        if token:
            res = urllib2.Request(
                'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' +
                token
            )

            with contextlib.closing(
                urllib2.urlopen(res, json.dumps(message_body,
                                                ensure_ascii=False))) as r:

                if r.code == 200:
                    print r.read()
                    return True
                else:
                    print r.code, r.read()
                    return False
        else:
            return False


def push_message(**kwargs):
    wxp = WeixinPush(CORPID, CORPSECRET)
    wxp.push_text_message(**kwargs)

if __name__ == '__main__':
    push_message(agentid=4, content='qyweixin api')
