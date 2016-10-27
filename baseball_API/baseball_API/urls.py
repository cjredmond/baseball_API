
from django.conf.urls import url
from django.contrib import admin
from stats.views import MasterListCreateAPIView, BattingListCreateAPIView, PitcherListCreateAPIView, FieldingListCreateAPIView, \
                        MasterDetailUpdateDestroyAPIView, BattingDetailUpdateDestroyAPIView, PitcherDetailUpdateDestroyAPIView, \
                        FieldingDetailUpdateDestroyAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/:masters/$', MasterListCreateAPIView.as_view(), name="master_list_create_api_view"),
    url(r'^api/:batters/$', BattingListCreateAPIView.as_view(), name="batting_list_create_api_view"),
    url(r'^api/:pitchers/$', PitcherListCreateAPIView.as_view(), name="pitcher_list_create_api_view"),
    url(r'^api/:fielders/$', FieldingListCreateAPIView.as_view(), name="fielding_list_create_api_view"),
    url(r'^api/:masters/(?P<pk>\d+)/$', MasterDetailUpdateDestroyAPIView.as_view(), name="master_detail_update_destroy_api_view"),
    url(r'^api/:batters/(?P<pk>\d+)/$', BattingDetailUpdateDestroyAPIView.as_view(), name="batting_detail_update_destroy_api_view"),
    url(r'^api/:pitchers/(?P<pk>\d+)/$', PitcherDetailUpdateDestroyAPIView.as_view(), name="pitcher_detail_update_destroy_api_view"),
    url(r'^api/:fielders/(?P<pk>\d+)/$', FieldingDetailUpdateDestroyAPIView.as_view(), name="fieling_detail_update_destroy_api_view"),
]
