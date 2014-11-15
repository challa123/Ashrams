__author__ = 'challa'

from django.db import models
from django.utils import timezone


class Base(models.Model):
    created_date = models.DateTimeField('created date', default=timezone.now())
    modified_date = models.DateTimeField('modified date', default=timezone.now())

    class Meta:
        abstract = True
