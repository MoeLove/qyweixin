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
__version__ = '0.1.2'
__license__ = 'GPL'
__copyright__ = 'Copyright 2015 TaoBeier'


import logging
from logging import NullHandler
from .get_token import AccessToken
from .push_message import WeixinPush

logging.getLogger(__name__).addHandler(NullHandler())
