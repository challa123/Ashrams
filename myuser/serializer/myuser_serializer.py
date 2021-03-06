from rest_framework import serializers
from myuser.models import MyUser

__author__ = 'challa'


class MyUserSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(source='created_date', required=False)
    modifiedDate = serializers.DateTimeField(source='modified_date', required=False)
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')
    profilePic = serializers.FileField(source='profile_pic', required=False)

    class Meta:
        model = MyUser
        fields = ('id', 'createdDate', 'modifiedDate', 'username', 'firstName', 'lastName',
                  'email', 'address', 'phone', 'groups', 'profilePic')