from rest_framework import serializers
from anonymoususer.models import AnonymousUser

__author__ = 'challa'


class AnonymousUserSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(source='created_date', required=False)
    modifiedDate = serializers.DateTimeField(source='modified_date', required=False)
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')

    class Meta:
        model = AnonymousUser
        fields = ('id', 'createdDate', 'modifiedDate', 'firstName', 'lastName',
                  'email', 'address', 'phone')