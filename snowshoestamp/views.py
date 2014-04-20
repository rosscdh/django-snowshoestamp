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
    template = None
    json_dumps_kwargs = {'indent': 3}

    def get(self, request, *args, **kwargs):
        context_dict = {
            'message': 'Please Post to this endpoint',
        }
        return self.render_json_response(context_dict)

    def post(self, request, *args, **kwargs):
        logger.info('Recieved snowshoestamp webhook')

        service = SnowshoeStampWebhookService()
        service.process(data=request.POST)

        custom_callback_view = getattr(settings, 'SNOWSHOESTAMP_CALLBACK_VIEW', None)

        if custom_callback_view is not None:
            # is it a new proper view
            if hasattr(custom_callback_view, 'as_view') is True:
                logger.info('Using custom CBV SNOWSHOESTAMP_CALLBACK_VIEW')
                return custom_callback_view.as_view()(self.request)

            else:
                # normal old style view
                logger.info('Using custom old-style SNOWSHOESTAMP_CALLBACK_VIEW')
                return custom_callback_view(request=request)
        #
        # no custom views defined, so just return 200
        # and thanks
        #
        logger.info('No custom CBV SNOWSHOESTAMP_CALLBACK_VIEW defined returning 200')
        return self.render_json_response({
            'details': 'Snowshoestamp Callback recieved'
        })