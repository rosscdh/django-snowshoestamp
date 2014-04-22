# -*- coding: utf-8 -*-
from django.conf import settings
from django.views.generic import View
from braces.views import JSONResponseMixin

from .services import SnowshoeStampWebhookService

import logging
logger = logging.getLogger('django.request')


class SnowshoeStampView(JSONResponseMixin, View):
    """
    Handle the snowshoestamp callback
    """
    http_method_names = [u'post',]

    json_dumps_kwargs = {'indent': 3}

    service = None
    stamp_serial = None
    stamp_data = None

    def dispatch(self, request, *args, **kwargs):
        logger.info('Recieved snowshoestamp webhook')
        self.service = SnowshoeStampWebhookService()

        if request.method.lower() in self.http_method_names:
            import pdb;pdb.set_trace()
            self.stamp_serial, self.stamp_data = self.service.process(data=request.POST)

        return super(SnowshoeStampView, self).dispatch(request=request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.render_json_response({
            'detail': 'Snowshoestamp Callback recieved',
            'serial': self.stamp_serial,
            'data': self.stamp_data,
        })