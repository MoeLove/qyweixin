qyweixin
=========

.. image:: https://img.shields.io/pypi/v/qyweixin.svg
    :target: https://pypi.python.org/pypi/qyweixin

`enterprise weixin <https://qy.weixin.qq.com>`_, interface.

Usage
--------

- get token

.. code-block:: python

    >>> import qyweixin
    >>> qy = qyweixin.AccessToken(corpid, corpsecret)
    >>> token = qy.get_token()
    >>> token
    ...


- push message

.. code-block:: python

    >>> push_msg = qyweixin.WeixinPush()
    >>> push_msg.push_text_msg(token=token, content='test msg')
    True


- upload files

.. code-block:: python

    >>> upload = qyweixin.Upload()
    >>> media_id = upload.upload(token, filename, filepath, filetype)
    ...


Features
--------

- uploads media
- manage media
- receive message
- more qyweixin api


Installation
--------

To install qyweixin, simply:

.. code-block:: bash

    $ pip install qyweixin
