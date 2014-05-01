# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt

from .views import SnowshoeStampView, SnowshoeStampHoldingView


urlpatterns = patterns('',
    url(r'^webhook/$', csrf_exempt(SnowshoeStampView.as_view()), name='snowshoestamp_webhook_callback'),
    url(r'^holding/(?P<content_object_type_id>[\d-]+)/(?P<object_id>[\d]+)/$', SnowshoeStampHoldingView.as_view(), name='snowshoestamp_holding'),
)
