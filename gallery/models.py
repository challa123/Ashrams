from django.db import models
from ashrams.models import Ashrams, Base


class Gallery(Base, models.Model):
    ashram_id = models.ForeignKey(Ashrams, null=True, blank=True)

    class Meta:
        app_label = 'gallery'

class Images(models.Model):
    image = models.FileField(upload_to='gallery')
    gallery = models.ForeignKey(Gallery)

    class Meta:
        app_label = 'gallery'




