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

    def test_init(self):
        qy = qyweixin.AccessToken('wx72942dxxx4', '6o_2i')
        token = qy.get_token()

        assert token is False


if __name__ == '__main__':
    unittest.main()
