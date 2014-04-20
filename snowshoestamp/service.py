# -*- coding: utf-8 -*-
from django.conf import settings
from sssapi import Client

SNOWSHOESTAMP_KEY = getattr(settings, 'SNOWSHOESTAMP_KEY', None)
SNOWSHOESTAMP_SECRET = getattr(settings, 'SNOWSHOESTAMP_SECRET', None)

assert SNOWSHOESTAMP_KEY, 'You must define a settings.SNOWSHOESTAMP_KEY'
assert SNOWSHOESTAMP_SECRET, 'You must define a settings.SNOWSHOESTAMP_SECRET'

from .signals import snowshoestamp_event


class SnowshoeStampWebhookService(object):
    client = None
    stamp_data = None
    stamp_serial = None

    def __init__(self, *args, **kwargs):
        # Allow overrides
        self.key = kwargs.get('key', SNOWSHOESTAMP_KEY)
        self.secret = kwargs.get('key', SNOWSHOESTAMP_SECRET)
        self.client = Client(self.key, self.secret)

    def process(self, data):
        """
        Method to process the callback data
        """
        self.stamp_data = data.get('stamp', None)

        if self.stamp_data is not None:

            # pop the stamp_serial from the data so its not repeated
            self.stamp_serial = stamp_data.pop('serial', None)

            if self.stamp_serial is not None:
                snowshoestamp_event.send(sender=self, stamp_serial=stamp_serial, **self.stamp_data)