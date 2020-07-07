from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
     re_path(r'ws/monitor/button/(?P<button_name>\w+)/$',consumers.ButtonClick),
    re_path(r'ws/monitor/axis/(?P<x>\w+)/get/(?P<y>\w+)/$',consumers.Coordinate),
    re_path(r'ws/monitor/right/(?P<x>\w+)/$',consumers.Right),
]
