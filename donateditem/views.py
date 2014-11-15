from rest_framework import generics, permissions
from donateditem.models import DonatedItem
from donateditem.serializer.donateditem_serializer import DonatedItemSerializer


class ListCreateDonatedItemView(generics.ListCreateAPIView):
    model = DonatedItem
    serializer_class = DonatedItemSerializer
    permission_classes = (permissions.AllowAny,)

class DonatedItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = DonatedItem
    serializer_class = DonatedItemSerializer
    permission_classes = (permissions.AllowAny,)