from gallery.views import ListGalleryView

__author__ = 'challa'

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = []

urlpatterns += format_suffix_patterns(
    patterns('gallery.views',
        url(r'^gallery/$', ListGalleryView.as_view(),name='gallery-list')
    )
)