from requireditem.views import ListRequiredItemView, RequiredItemDetailView

__author__ = 'challa'

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = []

urlpatterns += format_suffix_patterns(
    patterns('requireditem.views',
        url(r'^requireditem/$', ListRequiredItemView.as_view(),name='required-items-list'),
        url(r'^requireditem/(?P<pk>[-._a-zA-Z0-9]+)/$', RequiredItemDetailView.as_view(), name='required-item-detail')
    )
)