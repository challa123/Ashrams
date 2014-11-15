from rest_framework import serializers
from gallery.models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    ashramId = serializers.IntegerField(source='ashram_id', required=False)

    class Meta:
        model = Gallery
        fields = ('id', 'ashramId', 'pic')