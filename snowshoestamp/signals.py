# -*- coding: utf-8 -*-
"""
Webhook signals
"""
from django.dispatch import Signal, receiver

#
# Outgoing Events
#
snowshoestamp_event = Signal(providing_args=['stamp_serial'])
