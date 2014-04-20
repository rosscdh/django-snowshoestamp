# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt

from .views import SnowshoeStampView


urlpatterns = patterns('',
    url(r'^webhook/$', csrf_exempt(SnowshoeStampView.as_view()), name='snowshoestamp_webhook_callback'),
)
