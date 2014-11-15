from django.shortcuts import render, render_to_response
from rest_framework import generics, permissions
from ashrams.models import Ashrams
from ashrams.serializer.ashram_serializer import AshramSerializer


def sample_html(request):
    return render_to_response('home.html')

class ListAshramView(generics.ListAPIView):
    model = Ashrams
    serializer_class = AshramSerializer
    permission_classes = (permissions.AllowAny,)

class AshramDetailView(generics.RetrieveAPIView):
    model = Ashrams
    serializer_class = AshramSerializer
    permission_classes = (permissions.AllowAny,)