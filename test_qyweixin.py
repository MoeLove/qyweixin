#!/usr/bin/env python
# coding=utf-8

import os
import unittest

import qyweixin

TEST_TOKEN = 'xDxcn2bfGhG44dAum1OjbHwkmHZJYH1aM9ORNAhA0peABXgMkuxBKZ6qDvQkTGG3Yh_qr-fPcFnOfUpoYz9ZEA'


class QyweixinTestCase(unittest.TestCase):

    def test_push_text_msg_wrong_token(self):
        push_msg = qyweixin.WeixinPush()
        result = push_msg.push_text_msg('text_token')

        assert result is False

    def test_push_text_msg_correct_token(self):
        push_msg = qyweixin.WeixinPush()
        result = push_msg.push_text_msg(TEST_TOKEN, agentid=0,
                                        content='test_msg')

        assert result is True

    def test_upload_file_and_push_msg(self):
        if TEST_TOKEN:
            os.system('echo "test upload file for qyweixin" > test_qyweixin.txt')
            media_id = qyweixin.upload(TEST_TOKEN,
                                       'test_qyweixin.txt',
                                       'test_qyweixin.txt', 'file')

            push_msg = qyweixin.WeixinPush()
            result = push_msg.push_file_msg(TEST_TOKEN, agentid=0, media_id=media_id)

            assert media_id is not False
            assert result is True

            os.system('rm test_qyweixin.txt')

    def test_upload_img_and_push_msg(self):
        if TEST_TOKEN:
            os.system('wget https://avatars0.githubusercontent.com/u/14851244 -O logo.png')
            media_id = qyweixin.upload(TEST_TOKEN,
                                       'logo.png',
                                       'logo.png',
                                       'image')

            push_msg = qyweixin.WeixinPush()
            result = push_msg.push_image_msg(TEST_TOKEN, agentid=0, media_id=media_id)

            assert media_id is not False
            assert result is True

            os.system('rm logo.png')

    def test_get_token(self):
        token = qyweixin.get_token('wx72942dxxx4', '6o_2i')

        assert token is False


if __name__ == '__main__':
    unittest.main()
