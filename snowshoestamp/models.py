# -*- coding: utf-8 -*-
from django.db import models

from jsonfield import JSONField


class AssociatedSnowShoeStamp(models.Model):
    """
    Model to associate SnowShoeStamps with content objects
    Each stamp is unique to the content type and object.pk
    """
    # content type of the object, used to do lookups as .source_object
    content_object_type = models.ForeignKey('contenttypes.ContentType', db_index=True)
    # id of the specific object
    object_id = models.IntegerField(db_index=True)
    # associated snowshoestamp ID
    stamp_serial = models.CharField(max_length=128, db_index=True)
    # misc data
    data = JSONField(default={}, blank=True, null=True)

    class Meta:
        unique_together = ('content_object_type', 'object_id', 'stamp_serial',)

    @property
    def source_object(self):
        """
        Return the object refered to by content_object_type and content_object_id
        """
        return self.content_object_type.get_object_for_this_type(pk=self.object_id)

    def __unicode__(self):
        return '%s for (%s)' % (self.stamp_serial, self.source_object)