# -*- coding:utf-8 -*-

import contextlib
import urllib2

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
                      content={}, touser='@all', toparty='',
                      totag='', safe=0):
        message_body = {
            'touser': self._target_format(touser),
            'toparty': self._target_format(toparty),
            'totag': self._target_format(totag),
            'agentid': agentid,
            'msgtype': msgtype,
            msgtype: content,
            'safe': safe
        }

        if token:
            push_message_api = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % token
            res = urllib2.Request(push_message_api)

            with contextlib.closing(
                urllib2.urlopen(res, json.dumps(message_body,
                                                ensure_ascii=False))) as r:

                resp = json.loads(r.read())

                if resp.get('errmsg', None) == 'ok':
                    return True
                else:
                    return False
        else:
            return False

    def push_text_message(self, token=None, agentid=0, content='',
                          touser='@all', toparty='', totag='', safe=0):
        _text_content = {
            'content': content
        }

        return self._push_message(token=token, agentid=agentid, msgtype='text',
                                  content=_text_content, touser=touser,
                                  toparty=toparty, totag=totag, safe=safe)

    def push_image_message(self, token=None, agentid=0, media_id='',
                           touser='@all', toparty='', totag='', safe=0):
        _image_content = {
            'media_id': media_id
        }

        return self._push_message(token=token, agentid=agentid,
                                  msgtype='image', content=_image_content,
                                  touser=touser, toparty=toparty, totag=totag,
                                  safe=safe)

    def push_voice_message(self, token=None, agentid=0, media_id='',
                           touser='@all', toparty='', totag='', safe=0):
        _voice_content = {
            'media_id': media_id
        }

        return self._push_message(token=token, agentid=agentid,
                                  msgtype='voice', content=_voice_content,
                                  touser=touser, toparty=toparty, totag=totag,
                                  safe=safe)

    def push_video_message(self, token=None, agentid=0, media_id='', title='',
                           description='', touser='@all', toparty='',
                           totag='', safe=0):
        _video_content = {}
        _video_content['media_id'] = media_id
        _video_content['title'] = title
        _video_content['description'] = description

        return self._push_message(token=token, agentid=agentid,
                                  msgtype='video', content=_video_content,
                                  touser=touser, toparty=toparty,
                                  totag=totag, safe=safe)

    def push_file_message(self, token=None, agentid=0, media_id='',
                          touser='@all', toparty='', totag='', safe=0):
        _file_content = {
            'media_id': media_id
        }

        return self._push_message(token=token, agentid=agentid,
                                  msgtype='file', content=_file_content,
                                  touser=touser, toparty=toparty, totag=totag,
                                  safe=safe)
