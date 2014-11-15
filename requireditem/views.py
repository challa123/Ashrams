from rest_framework import generics, permissions
from requireditem.models import RequiredItem
from requireditem.serializer import RequiredItemSerializer


class ListRequiredItemView(generics.ListAPIView):
    model = RequiredItem
    serializer_class = RequiredItemSerializer
    permission_classes = (permissions.AllowAny,)

class RequiredItemDetailView(generics.RetrieveAPIView):
    model = RequiredItem
    serializer_class = RequiredItemSerializer
    permission_classes = (permissions.AllowAny,)