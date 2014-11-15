from django.db import models
from ashrams.models import Base, Ashrams
from myuser.models import MyUser
from requireditem.models import RequiredItem


class DonatedItem(Base, models.Model):
    to_be_picked = 0
    to_be_delivered = 1
    delivered = 2

    STATUS_CHOICE_OPTIONS = (
        (to_be_picked, 'To be picked'),
        (to_be_delivered, 'To be delivered'),
        (delivered, 'delivered')
    )

    name = models.CharField(max_length=512)
    description = models.TextField()
    quantity = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(max_length=1, default=0, choices=STATUS_CHOICE_OPTIONS)
    delivered_date = models.DateTimeField(null=True, blank=True)
    available_time = models.DateTimeField(null=True, blank=True)
    ashram_id = models.ForeignKey(Ashrams, null=True, blank=True, verbose_name='ashram')
    user = models.ForeignKey(MyUser, verbose_name='user')
    is_anonymous = models.BooleanField(default=True)
    image_by_user = models.FileField(null=True, blank=True, upload_to='donated/user')
    image_by_ashram = models.FileField(null=True, blank=True, upload_to='donated/ashram')
    required_item = models.ForeignKey(RequiredItem, null=True, blank=True)

    class Meta:
        app_label = 'donateditem'
