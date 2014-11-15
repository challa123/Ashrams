from django.db import models
from ashrams.models import Base, Ashrams


class AnonymousUser(Base, models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    address = models.TextField(blank=True, null=True)
    phone = models.IntegerField(max_length=10)
    email = models.CharField(
        verbose_name='email',
        max_length=255, null=True, blank=True
    )

    class Meta:
        app_label = 'anonymoususer'
