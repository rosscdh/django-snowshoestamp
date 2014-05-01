# -*- coding: utf-8 -*-
from django.conf import settings
from sssapi import Client

SNOWSHOESTAMP_KEY = getattr(settings, 'SNOWSHOESTAMP_KEY', None)
SNOWSHOESTAMP_SECRET = getattr(settings, 'SNOWSHOESTAMP_SECRET', None)

assert SNOWSHOESTAMP_KEY, 'You must define a settings.SNOWSHOESTAMP_KEY'
assert SNOWSHOESTAMP_SECRET, 'You must define a settings.SNOWSHOESTAMP_SECRET'

from .signals import snowshoestamp_event

import logging
logger = logging.getLogger('django.request')


class SnowshoeStampWebhookService(object):
    client = None
    stamp_data = None
    stamp_serial = None

    def __init__(self, *args, **kwargs):
        # Allow overrides
        self.key = kwargs.get('key', SNOWSHOESTAMP_KEY)
        self.secret = kwargs.get('secret', SNOWSHOESTAMP_SECRET)
        self.client = Client(self.key, self.secret)
        logger.info('Initialized sssapi.Client with key: %s' % self.key)
        self.stamp_data = None
        self.stamp_serial = None

    def process(self, data):
        """
        Method to process the callback data
        """
        data = self.client.call({'data': data.get('data')})

        self.stamp_data = data.get('stamp', None)

        if self.stamp_data is not None:
            logger.info('Provided with stamp data: %s' % data)
            # pop the stamp_serial from the data so its not repeated
            self.stamp_serial = self.stamp_data.pop('serial', None)
            logger.info('Provided with stamp serial: %s' % self.stamp_serial)

            # issue the signal
            #if self.stamp_serial is not None:
            snowshoestamp_event.send(sender=self, stamp_serial=self.stamp_serial, **data)

        return (self.stamp_serial, data)