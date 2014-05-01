# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.views.generic.list import MultipleObjectMixin
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from braces.views import JSONResponseMixin

from .services import SnowshoeStampWebhookService
from .models import AssociatedSnowShoeStamp

import json
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
            self.stamp_serial, self.stamp_data = self.service.process(data=request.POST)

        return super(SnowshoeStampView, self).dispatch(request=request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.render_json_response({
            'detail': 'Snowshoestamp Callback recieved',
            'serial': self.stamp_serial,
            'data': self.stamp_data,
        })


class SnowshoeStampHoldingView(TemplateView, MultipleObjectMixin):
    """
    Holding page for user to wait on for a pusher event that will redirect to requested page
    """
    model = AssociatedSnowShoeStamp
    template_name = 'snowshoestamp/holding.html'

    def get_queryset(self):
        content_object_type_id = self.kwargs.get('content_object_type_id')
        object_id = self.kwargs.get('object_id')

        self.content_object = get_object_or_404(ContentType, pk=content_object_type_id)
        self.source_object = self.content_object.get_object_for_this_type(pk=object_id)

        return self.model.objects.filter(content_object_type=self.content_object, object_id=object_id)

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        kwargs.update({
            'object_list': self.object_list,
            'content_object': self.content_object,
            'source_object': self.source_object,
        })

        return super(SnowshoeStampHoldingView, self).get_context_data(**kwargs)

    def post(self, request, **kwargs):
        stamp_found = self.get_queryset().filter(stamp_serial=request.POST['stamp_serial']).first()

        if stamp_found is None:
            raise Http404

        return HttpResponse(json.dumps({'redirect': self.source_object.get_absolute_url()}), content_type='application/json')
