# -*- coding:utf-8 -*-

import contextlib
import json
import urllib2

from config import AGENTID, CORPID, CORPSECRET


class WeixinPush(object):

    def __init__(self, corpid, corpsecret):
        self.corpid = corpid
        self.corpsecret = corpsecret

    def get_token(self):
        res = urllib2.Request(self._get_url('get_token',
                                            corpid=self.corpid,
                                            corpsecret=self.corpsecret))

        with contextlib.closing(urllib2.urlopen(res)) as r:
            resp = json.loads(r.read())

            if resp.get('access_token', None):
                return resp['access_token']
            else:
                print resp
                return

    def _target_format(self, target):
        if isinstance(target, list):
            return '|'.join(target)
        else:
            return target

    def push_text_message(self, agentid=AGENTID, content='', touser='@all',
                          toparty='', totag='', **kwargs):
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

        token = self.get_token()

        if token:
            res = urllib2.Request(self._get_url('push_message', token=token))

            with contextlib.closing(
                urllib2.urlopen(res, json.dumps(message_body,
                                                ensure_ascii=False))) as r:

                if r.code == 200:
                    print r.read()
                    return True
                else:
                    print r.code, r.read()
                    return False

    def _get_url(self, api_name, **kwargs):
        api_collections = {
            'get_token': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + kwargs.get('corpid', '') + '&corpsecret=' + kwargs.get('corpsecret', ''),
            'push_message': 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + kwargs.get('token', '')
        }

        return api_collections[api_name]


def push_message(**kwargs):
    wxp = WeixinPush(CORPID, CORPSECRET)
    wxp.push_text_message(**kwargs)

if __name__ == '__main__':
    push_message(agentid=4, content='qyweixin api')
