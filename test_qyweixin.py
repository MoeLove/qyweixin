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

import qyweixin


class QyweixinTestCase(unittest.TestCase):

    def test_get_token(self):
        token = qyweixin.get_token('wx72942dxxx4', '6o_2i')

        assert token is False

    def test_push_text_msg(self):
        push_msg = qyweixin.WeixinPush()
        result = push_msg.push_text_msg('text_token')

        assert result is False


if __name__ == '__main__':
    unittest.main()
