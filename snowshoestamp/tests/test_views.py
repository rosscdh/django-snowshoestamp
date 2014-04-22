# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from django.core.urlresolvers import reverse_lazy

from snowshoestamp.views import SnowshoeStampView


class SnowshoeStampViewTest(TestCase):
    subject = SnowshoeStampView

    def setUp(self):
        self.client = Client()
        self.url = reverse_lazy('snowshoestamp_webhook_callback')
        self.valid_webhook_data = {
            'data': {
                'stamp': {
                    'serial': '123456789',
                    'key': 'value',
                }
            }
        }

    def test_invalid_methods(self):
        invalid_methods = [u'get', u'put', u'patch', u'delete', u'head', u'options', u'trace']
        for m in invalid_methods:
            if hasattr(self.client, m):
                resp = getattr(self.client, m)(self.url, self.valid_webhook_data)
                self.assertEqual(resp.status_code, 405)

    def test_valid_method(self):
        resp = self.client.post(self.url, self.valid_webhook_data)
        self.assertEqual(resp.status_code, 200))