from django.urls import path 
from .consumers import JokesConsumer

ws_urlpatterns = [ 
    path('ws/joke/', JokesConsumer.as_asgi())
]