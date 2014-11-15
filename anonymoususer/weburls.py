from anonymoususer.views import ListAnonymousUserView, AnonymousUserDetailView

__author__ = 'challa'

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = []

urlpatterns += format_suffix_patterns(
    patterns('anonymoususer.views',
        url(r'^donateditem/$', ListAnonymousUserView.as_view(),name='anonymoususers-list'),
        url(r'^donateditem/(?P<pk>[-._a-zA-Z0-9]+)/$', AnonymousUserDetailView.as_view(), name='anonymoususer-detail')
    )
)