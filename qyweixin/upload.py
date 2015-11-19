# -*- coding:utf-8 -*-

import base64
import contextlib
import json
import mimetypes
import os
import urllib2


class Upload(object):

    """"
    This class can upload files to weixin server.
    Support image, voice, video and other files.
    """

    def _encode_multipart_data(self):
        """
        The code is from https://github.com/tao12345666333/httpmultipart
        """
        BOUNDARY = ''.join(['-----', base64.urlsafe_b64encode(os.urandom(27))])
        CRLF = '\r\n'
        line = []

        for (key, value) in self.fields:
            line.append('--' + BOUNDARY)
            line.append('Content-Disposition: form-data; name="%s"' % key)
            line.append('')
            line.append(value)

        for (key, filename, filepath) in self.files:
            line.append('--' + BOUNDARY)
            line.append(
                'Content-Disposition: form-data; name="%s"; filename="%s"' %
                (key, filename))
            line.append(
                'Content-Type: %s' %
                (mimetypes.guess_type(filename)[0] or 'application/octet-stream'))
            line.append('')
            line.append(open(filepath, 'rb').read())

        line.append('--' + BOUNDARY + '--')
        line.append('')

        body = CRLF.join(line)
        content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
        return content_type, body

    def upload(self, token, filename, filepath, filetype):
        """
        This function can upload files to weixin server and return 'media_id',
        which can push to user's message.
        """
        self.url = 'https://qyapi.weixin.qq.com/cgi-bin/media/upload'
        self.fields = [
            ('access_token', token.encode('utf-8')), ('type', filetype)]
        self.files = [('media', filename, filepath)]

        req = urllib2.Request(url=self.url)
        contentType, body = self._encode_multipart_data()

        req.add_header('Content-Length', '%d' % len(body))
        req.add_header('Content-Type', '%s' % contentType)
        with contextlib.closing(urllib2.urlopen(req, data=body)) as r:
            resp = json.loads(r.read())
            return resp.get('media_id', False)


def upload(token, filename, filepath, filetype):
    """
    This function can upload files to weixin server and return 'media_id',
    which can push to user's message.
    """
    qyupload = Upload()
    return qyupload.upload(token, filename, filepath, filetype)
