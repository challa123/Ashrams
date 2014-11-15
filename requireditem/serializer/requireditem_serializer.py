__author__ = 'challa'

from rest_framework import serializers
from requireditem.models import RequiredItem


class RequiredItemSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(source='created_date', required=False)
    modifiedDate = serializers.DateTimeField(source='modified_date', required=False)
    ashramId = serializers.IntegerField(source='ashram_id')

    class Meta:
        model = RequiredItem
        fields = ('id', 'createdDate', 'modifiedDate', 'name', 'description', 'quantity', 'ashramId')
