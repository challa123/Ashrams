from ashrams.views import ListAshramView, AshramDetailView

__author__ = 'challa'

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = []

urlpatterns += format_suffix_patterns(
    patterns('ashrams.views',
        url(r'^ashrams/$', ListAshramView.as_view(),name='ashrams-list'),
        url(r'^ashrams/(?P<pk>[-._a-zA-Z0-9]+)/$', AshramDetailView.as_view(), name='ashram-detail')
    )
)