# -*- coding:utf-8 -*-

import contextlib
import urllib2

try:
    import json
except ImportError:
    import simplejson as json


class WeixinPush(object):
    """
    You need get a instance for push message.
    """

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
        }

        if msgtype != 'news':
            message_body['safe'] = safe

        if token:
            push_message_api = ('https://qyapi.weixin.qq.com/cgi-bin/message'
                                '/send?access_token={token}').format(
                                    token=token)
            res = urllib2.Request(push_message_api)

            with contextlib.closing(
                urllib2.urlopen(res, json.dumps(message_body,
                                                ensure_ascii=False))) as r:

                resp = json.loads(r.read())

                # 2017.06.15 update:
                # error judge
                if resp.get('errmsg', None) == 'ok' and \
                        resp.get('errcode', None) == 0 and \
                        resp.get('invaliduser', '') == '' and \
                        resp.get('invalidparty', '') == '':
                    return True
                else:
                    return False, resp
        else:
            return False, {'errmsg': 'token is needed'}

    def push_text_msg(self, token, agentid=0, content='',
                      touser='@all', toparty='', totag='', safe=0):
        _text_content = {
            'content': content
        }

        return self._push_message(token=token, agentid=agentid, msgtype='text',
                                  content=_text_content, touser=touser,
                                  toparty=toparty, totag=totag, safe=safe)

    def push_image_msg(self, token, agentid=0, media_id='',
                       touser='@all', toparty='', totag='', safe=0):
        _image_content = {
            'media_id': media_id
        }

        return self._push_message(token=token, agentid=agentid,
                                  msgtype='image', content=_image_content,
                                  touser=touser, toparty=toparty, totag=totag,
                                  safe=safe)

    def push_voice_msg(self, token, agentid=0, media_id='',
                       touser='@all', toparty='', totag='', safe=0):
        _voice_content = {
            'media_id': media_id
        }

        return self._push_message(token=token, agentid=agentid,
                                  msgtype='voice', content=_voice_content,
                                  touser=touser, toparty=toparty, totag=totag,
                                  safe=safe)

    def push_video_msg(self, token, agentid=0, media_id='', title='',
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

    def push_file_msg(self, token, agentid=0, media_id='',
                      touser='@all', toparty='', totag='', safe=0):
        _file_content = {
            'media_id': media_id
        }

        return self._push_message(token=token, agentid=agentid,
                                  msgtype='file', content=_file_content,
                                  touser=touser, toparty=toparty, totag=totag,
                                  safe=safe)

    def push_news_msg(self, token, agentid=0, articles=None,
                      touser='@all', toparty='', totag=''):
        """The articles params format eg.
            articles = [
                {
                    "title": "Title",
                    "description": "Description",
                    "url": "URL",
                    "picurl": "PIC_URL"
                },
            ]
        """

        if not articles or len(articles) == 0:
            raise Exception('the articles at least include one content')

        # TODO: format verify
        _news_content = {
            'articles': articles
        }

        return self._push_message(token=token, agentid=agentid,
                                  msgtype='news', content=_news_content,
                                  touser=touser, toparty=toparty, totag=totag)

    def push_one_news_msg(self, token, agentid=0, title='', description='',
                          url='', picurl='', touser='@all', toparty='',
                          totag=''):
        _news_content = {
            'articles': [
                {
                    'title': title,
                    'description': description,
                    'url': url,
                    'picurl': picurl
                }
            ]
        }

        return self._push_message(token=token, agentid=agentid,
                                  msgtype='news', content=_news_content,
                                  touser=touser, toparty=toparty, totag=totag)

    def push_mpnews_msg(self, token, agentid=0, articles=None,
                        media_id='', touser='@all', toparty='', totag='',
                        safe=0):

        # TODO: format verify
        if articles:
            _mpnews_content = {
                'articles': articles
            }
        elif media_id:
            _mpnews_content = {
                'media_id': media_id
            }
        else:
            raise Exception('params error')

        return self._push_message(token=token, agentid=agentid,
                                  msgtype='mpnews', content=_mpnews_content,
                                  touser=touser, toparty=toparty, totag=totag)

    def push_one_mpnews_msg(self, token, agentid=0, title='', thumb_media_id='',
                            author='', content_source_url='', content='',
                            digest='', show_cover_pic='', media_id='',
                            touser='@all', toparty='', totag='', safe=0):

        if media_id:
            _mpnews_content = {
                'media_id': media_id
            }
        else:
            _mpnews_content = {
                'articles': [
                    {
                        'title': title,
                        'thumb_media_id': thumb_media_id,
                        'author': author,
                        'content_source_url': content_source_url,
                        'content': content,
                        'digest': digest,
                        'show_cover_pic': show_cover_pic,
                    }
                ]
            }

        return self._push_message(token=token, agentid=agentid,
                                  msgtype='mpnews', content=_mpnews_content,
                                  touser=touser, toparty=toparty, totag=totag)
