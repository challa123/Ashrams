from rest_framework import generics, permissions
from gallery.models import Gallery
from gallery.serializer.gallery_serializer import GallerySerializer


class ListGalleryView(generics.ListCreateAPIView):
    model = Gallery
    serializer_class = GallerySerializer
    permission_classes = (permissions.AllowAny,)
