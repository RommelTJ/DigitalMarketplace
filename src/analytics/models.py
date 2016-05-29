from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from tags.models import Tag

# Create your models here.

class TagView(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    tag = models.ForeignKey(Tag)
    count = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.tag.title)