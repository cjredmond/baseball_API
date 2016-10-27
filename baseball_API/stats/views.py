from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from stats.models import Master, Pitcher, Fielding, Batting
from stats.serializers import MasterSerializer, PitcherSerializer, FieldingSerializer, BattingSerializer


class MasterListCreateAPIView(ListCreateAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer
    #paginate
class MasterDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

class BattingListCreateAPIView(ListCreateAPIView):
    queryset = Batting.objects.all()
    serializer_class = BattingSerializer

class BattingDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Batting.objects.all()
    serializer_class = BattingSerializer

class PitcherListCreateAPIView(ListCreateAPIView):
    queryset = Pitcher.objects.all()
    serializer_class = PitcherSerializer

class PitcherDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Pitcher.objects.all()
    serializer_class = PitcherSerializer

class FieldingListCreateAPIView(ListCreateAPIView):
    queryset = Fielding.objects.all()
    serializer_class = FieldingSerializer

class FieldingDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Fielding.objects.all()
    serializer_class = FieldingSerializer
