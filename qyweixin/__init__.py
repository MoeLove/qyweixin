# -*- coding:utf-8 -*-
"""
qyweixin
~~~~~~~~~~~~~~~~~~~
Interface for enterprise weixin
(https://qy.weixin.qq.com/)

Homepage:
    http://github.com/MoeLove/qyweixin

"""

__title__ = 'qyweixin'
__author__ = 'TaoBeier'
__version__ = '0.3.0'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015-2016 TaoBeier'


import logging
from logging import NullHandler
from .get_token import get_token
from .push_message import WeixinPush
from .upload import upload

logging.getLogger(__name__).addHandler(NullHandler())
