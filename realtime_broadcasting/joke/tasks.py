import requests 
from time import sleep 
from celery import shared_task 

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync 

channel_layer = get_channel_layer() # return async func.

@shared_task
def get_joke():
    url = 'http://api.icndb.com/jokes/random/'
    resp = requests.get(url).json()
    joke = resp['value']['joke']

    async_to_sync(channel_layer.group_send)("jokes", {"type": "send_jokes", "text": joke})

