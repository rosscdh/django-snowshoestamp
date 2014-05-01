# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from django.core.urlresolvers import reverse_lazy

from snowshoestamp.views import SnowshoeStampView

from . import (TRANSLATED_WEBHOOK_DATA,
               WEBHOOK_POSTED_DATA,
               VALID_VIEW_RESPONSE)

import json
import httpretty


class SnowshoeStampViewTest(TestCase):
    """
    {"stamp": {"serial": "DEV-STAMP"}, "receipt": "2DJ2fkRJQdGhaLwLjIZL9Zpz/84=", "secure": false, "created": "2014-04-26 14:35:43.543350"}
    which gets encoded by snowshoestamp as
    W1syNjgsMjc5XSxbMjYzLDEwN10sWzk0LDUxXSxbOTQsMjgwXSxbMjA0LDQ5XV0%3D
    """
    subject = SnowshoeStampView

    def setUp(self):
        self.client = Client()
        self.url = reverse_lazy('snowshoestamp_webhook_callback')
        self.valid_webhook_data = WEBHOOK_POSTED_DATA

    def test_invalid_methods(self):
        invalid_methods = [u'get', u'put', u'patch', u'delete', u'head', u'options', u'trace']
        for m in invalid_methods:
            if hasattr(self.client, m):
                resp = getattr(self.client, m)(self.url, self.valid_webhook_data)
                self.assertEqual(resp.status_code, 405)

    @httpretty.activate
    def test_valid_method(self, *args, **kwargs):
        httpretty.register_uri(httpretty.POST, "http://beta.snowshoestamp.com/api/v2/stamp",
                       body=json.dumps(TRANSLATED_WEBHOOK_DATA),
                       status=200)

        resp = self.client.post(self.url, self.valid_webhook_data)
        self.assertEqual(resp.status_code, 200)

        self.assertEqual(json.loads(resp.content), VALID_VIEW_RESPONSE)
