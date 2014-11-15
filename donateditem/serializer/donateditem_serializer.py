from rest_framework import serializers
from donateditem.models import DonatedItem


class DonatedItemSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(source='created_date', required=False)
    modifiedDate = serializers.DateTimeField(source='modified_date', required=False)
    deliveredDate = serializers.DateTimeField(source='delivered_date', required=False)
    availableTime = serializers.DateTimeField(source='available_time', required=False)
    imageByUser = serializers.FileField(source='image_by_user', required=False)
    imageByAshram = serializers.FileField(source='image_by_ashram', required=False)
    isAnonymous = serializers.BooleanField(source='is_anonymous', default=True)
    requiredItem = serializers.IntegerField(source='required_item', required=False)
    userId = serializers.IntegerField(source='user_id')
    ashramId = serializers.IntegerField(source='ashram_id', required=False)

    class Meta:
        model = DonatedItem
        fields = ('id', 'createdDate', 'modifiedDate', 'name', 'description', 'quantity', 'deliveredDate',
                  'status', 'availableTime', 'ashramId', 'userId', 'imageByUser', 'imageByAshram', 'is_anonymous',
                  'requiredItem')