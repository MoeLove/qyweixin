qyweixin
=========

.. image:: https://img.shields.io/pypi/v/qyweixin.svg
    :target: https://pypi.python.org/pypi/qyweixin

.. image:: https://travis-ci.org/MoeLove/qyweixin.svg?branch=master
    :target: https://travis-ci.org/MoeLove/qyweixin

.. image:: https://coveralls.io/repos/MoeLove/qyweixin/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/MoeLove/qyweixin?branch=master

.. image:: https://img.shields.io/pypi/dm/qyweixin.svg
    :target: https://pypi.python.org/pypi/qyweixin

.. image:: https://img.shields.io/pypi/wheel/qyweixin.svg
    :target: https://pypi.python.org/pypi/qyweixin

.. image:: https://img.shields.io/pypi/status/qyweixin.svg
    :target: https://pypi.python.org/pypi/qyweixin

`Enterprise weixin <https://qy.weixin.qq.com>`_, interface.

Usage
--------

- get token

.. code-block:: python

    >>> import qyweixin
    >>> token = qyweixin.get_token('corpid', 'corpsecret')
    >>> token
    ...


- push message

.. code-block:: python

    >>> import qyweixin
    >>> push_msg = qyweixin.WeixinPush()
    >>> push_msg.push_text_msg(token=token, agentid=0, content='test msg', touser='test', toparty='test_group', totag='', safe=0)
    True


- upload files

.. code-block:: python

    >>> import qyweixin
    >>> media_id = qyweixin.upload(token, filename, filepath, filetype)
    ...


Features
---------

- push messages
- uploads media
- manage media
- more qyweixin api


Installation
-------------

To install qyweixin, simply:

.. code-block:: bash

    $ pip install qyweixin


Notice
--------

This package on v0.3.0 has one broken api. When the message fails to send, the details are returned.


License
=========

Copyright (C) 2015-2017 TaoBeier
