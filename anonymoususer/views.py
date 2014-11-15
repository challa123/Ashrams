from rest_framework import generics, permissions
from anonymoususer.models import AnonymousUser
from anonymoususer.serializer import AnonymousUserSerializer


class ListAnonymousUserView(generics.ListAPIView):
    model = AnonymousUser
    serializer_class = AnonymousUserSerializer
    permission_classes = (permissions.AllowAny,)

class AnonymousUserDetailView(generics.RetrieveAPIView):
    model = AnonymousUser
    serializer_class = AnonymousUserSerializer
    permission_classes = (permissions.AllowAny,)