from django.urls import re_path 
from .consumers import WSConsumer

ws_urlpatterns = [ 
    re_path('ws/integers/', WSConsumer.as_asgi()),
]