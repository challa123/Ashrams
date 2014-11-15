from django.db import models
from ashrams.models import Base, Ashrams


class RequiredItem(Base, models.Model):

    name = models.CharField(max_length=512)
    description = models.TextField()
    quantity = models.IntegerField(blank=True, null=True)
    ashram_id = models.ForeignKey(Ashrams, verbose_name='ashram')

    class Meta:
        app_label = 'requireditem'

    def __unicode__(self):
        return str(self.id)