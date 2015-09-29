# -*- coding:utf-8 -*-

import contextlib
import urllib2

from config import CORPID, CORPSECRET

try:
    import json
except ImportError:
    import simplejson as json


class WeixinPush(object):

    def _target_format(self, target):
        if isinstance(target, list):
            return '|'.join(target)
        else:
            return target

    def _push_message(self, token=None, agentid=0, msgtype='text',
                      content='', touser='@all', toparty='',
                      totag='', safe=0):
        message_body = {
            'touser': self._target_format(touser),
            'toparty': self._target_format(toparty),
            'totag': self._target_format(totag),
            'agentid': agentid,
            'msgtype': msgtype,
            'content': content,
            'safe': safe
        }

        if token:
            push_message_api = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + token
            res = urllib2.Request(push_message_api)

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

    def push_text_message(self, token=None, agentid=0, content='',
                          touser='@all', toparty='', totag='', safe=0):

        return self._push_message(token=token, agentid=agentid, msgtype='text',
                                  content=content, touser=touser,
                                  toparty=toparty, totag=totag, safe=safe)

    def push_image_message(self, token=None, agentid=0, content='',
                           touser='@all', toparty='', totag='', safe=0):

        return self._push_message(token=token, agentid=agentid,
                                  msgtype='image', content=content,
                                  touser=touser, toparty=toparty, totag=totag,
                                  safe=safe)

    def push_voice_message(self, token=None, agentid=0, content='',
                           touser='@all', toparty='', totag='', safe=0):

        return self._push_message(token=token, agentid=agentid,
                                  msgtype='voice', content=content,
                                  touser=touser, toparty=toparty, totag=totag,
                                  safe=safe)

    def push_video_message(self, token=None, agentid=0, media_id='', title='',
                           description='', touser='@all', toparty='',
                           totag='', safe=0):
        if media_id:
            content = {}
            content['media_id'] = media_id
            content['title'] = title
            content['description'] = description

            return self._push_message(token=token, agentid=agentid,
                                      msgtype='video', content=content,
                                      touser=touser, toparty=toparty, totag=totag,
                                      safe=safe)
        else:
            return False

    def push_file_message(self, token=None, agentid=0, content='',
                          touser='@all', toparty='', totag='', safe=0):

        return self._push_message(token=token, agentid=agentid,
                                  msgtype='file', content=content,
                                  touser=touser, toparty=toparty, totag=totag,
                                  safe=safe)


def push_message(**kwargs):
    wxp = WeixinPush(CORPID, CORPSECRET)
    wxp.push_text_message(**kwargs)

if __name__ == '__main__':
    push_message(agentid=4, content='qyweixin api')
