# -*- coding: utf-8 -*-
TRANSLATED_WEBHOOK_DATA = {"stamp": {"serial": "DEV-STAMP"}, "receipt": "2DJ2fkRJQdGhaLwLjIZL9Zpz/84=", "secure": False, "created": "2014-04-26 14:35:43.543350"}
WEBHOOK_POSTED_DATA = {'data': u'W1syODAsMjgxXSxbMjY3LDExMF0sWzkzLDU3XSxbMjAzLDUxXSxbMTAzLDI5MV1d'}

VALID_VIEW_RESPONSE = {u'serial': u'DEV-STAMP', u'data': {u'stamp': {}, u'receipt': u'2DJ2fkRJQdGhaLwLjIZL9Zpz/84=', u'secure': False, u'created': u'2014-04-26 14:35:43.543350'}, u'detail': u'Snowshoestamp Callback recieved'}

from .test_views import *
from .test_services import *
from .test_signals import *