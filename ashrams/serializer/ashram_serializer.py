from ashrams.models import Ashrams

__author__ = 'challa'
from rest_framework import serializers


class AshramSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(source='created_date', required=False)
    modifiedDate = serializers.DateTimeField(source='modified_date', required=False)
    belowOne = serializers.IntegerField(source='below_one', default=0)
    oneToFive = serializers.IntegerField(source='one_to_five', default=0)
    sixToTen = serializers.IntegerField(source='six_to_ten', default=0)
    elevenToFourteen = serializers.IntegerField(source='eleven_to_fourteen', default=0)
    fifteenToEighteen = serializers.IntegerField(source='fifteen_to_eighteen', default=0)
    nineteenToForty = serializers.IntegerField(source='nineteen_to_forty', default=0)
    fortyToSixty = serializers.IntegerField(source='forty_to_sixty', default=0)
    aboveSixty = serializers.IntegerField(source='above_sixty', default=0)
    ashramRating = serializers.IntegerField(source='ashram_rating')
    ashramPic = serializers.FileField(source='ashram_pic', required=False)
    userId = serializers.IntegerField(source='user_id')

    class Meta:
        model = Ashrams
        fields = ('id', 'createdDate', 'modifiedDate', 'name', 'address', 'info', 'phone', 'belowOne', 'oneToFive',
                  'sixToTen', 'elevenToFourteen', 'userId', 'fifteenToEighteen', 'nineteenToForty', 'fortyToSixty',
                  'aboveSixty', 'ashramRating', 'ashramPic', 'strength')