qyweixin
=========

.. image:: https://img.shields.io/pypi/v/qyweixin.svg
    :target: https://pypi.python.org/pypi/qyweixin

.. image:: https://img.shields.io/pypi/dm/qyweixin.svg
    :target: https://pypi.python.org/pypi/qyweixin

`enterprise weixin <https://qy.weixin.qq.com>`_, interface.

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
- receive message
- more qyweixin api


Installation
-------------

To install qyweixin, simply:

.. code-block:: bash

    $ pip install qyweixin


License
=========

Copyright (C) 2015 TaoBeier


HISTORY
=========

* 2015.09.27 Start.
* 2015.10.08 Add file upload.
