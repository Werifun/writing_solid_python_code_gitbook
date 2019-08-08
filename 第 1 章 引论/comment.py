"""
Requests HTTP library
~~~~~~~~~~~~~~~~~~~~~
Requests is an HTTP library, written in Python, for human beings. Basic GET
usage:
   >>> import requests
   >>> r = requests.get('https://www.python.org')
   >>> r.status_code
   200
   >>> 'Python is a programming language' in r.content
   True
... or POST:
   >>> payload = dict(key1='value1', key2='value2')
   >>> r = requests.post('http://httpbin.org/post', data=payload)
   >>> print(r.text)
   {
     ...
     "form": {
       "key2": "value2",
       "key1": "value1"
     },
     ...
   }
The other HTTP methods are supported - see `requests.api`. Full documentation
is at <http://python-requests.org>.
:copyright: (c) 2015 by Kenneth Reitz.
:license: Apache 2.0, see LICENSE for more details.
"""







"""
    Licensed Materials - Property of CorpA
    (C) CopyRight A Corp. 1999,2019 All Rights Reserved
    CopyRight statement ant purpose...
-------------------------------------------------------------------------------
File Name: comment.py
Description: description what the main function of this file
Author: author name
Change Activity: list of the change activity and time and author infomation

"""