from donateditem.views import DonatedItemDetailView, ListCreateDonatedItemView

__author__ = 'challa'

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = []

urlpatterns += format_suffix_patterns(
    patterns('donateditem.views',
        url(r'^donateditem/$', ListCreateDonatedItemView.as_view(),name='donated-items-list'),
        url(r'^donateditem/(?P<pk>[-._a-zA-Z0-9]+)/$', DonatedItemDetailView.as_view(), name='donated-item-detail')
    )
)