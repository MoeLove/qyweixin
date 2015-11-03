#!/usr/bin/env python
# coding=utf-8

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        raise

import unittest
import os

import qyweixin

TEST_TOKEN = 'F7BDI83twIdkvYoocoxB5DgXLiv69_H_OW_M758NQqxl3rL1uzSDJ6VrdEgwOr4WikApPVJgSqSEvwGyoi8bWw'


class QyweixinTestCase(unittest.TestCase):

    def test_get_token(self):
        token = qyweixin.get_token('wx72942dxxx4', '6o_2i')

        assert token is False

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


if __name__ == '__main__':
    unittest.main()
