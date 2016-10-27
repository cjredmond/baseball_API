from rest_framework import serializers
from stats.models import Master, Pitcher, Batting, Fielding

class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'

class PitcherSerializer(serializers.ModelSerializer):
    class Meta:
        player = serializers.HyperlinkedRelatedField(
        view_name = 'master_detail_update_destroy_api_view',
        read_only = True
        )

        model = Pitcher
        fields = '__all__'

class BattingSerializer(serializers.ModelSerializer):
    obp = serializers.CharField(max_length=100)
    class Meta:
        model = Batting
        fields = '__all__'

class FieldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fielding
        fields = '__all__'
