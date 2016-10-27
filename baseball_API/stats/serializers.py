from rest_framework import serializers
from stats.models import Master, Pitcher, Batting, Fielding

class MasterSerializer(serializers.ModelSerializer):
     class Meta:
        model = Master
        fields = '__all__'

class PitcherSerializer(serializers.ModelSerializer):
     class Meta:
        model = Pitcher
        fields = '__all__'

class BattingSerializer(serializers.ModelSerializer):
     class Meta:
        model = Batting
        fields = '__all__'

class FieldingSerializer(serializers.ModelSerializer):
     class Meta:
        model = Fielding
        fields = '__all__'
