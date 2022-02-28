import threading 
import time 

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync 

channel_layer = get_channel_layer() # return async func.

class Publisher(threading.Thread):
    def __init__(self, reply_channel, frequency=0.5):
        super(Publisher, self).__init__()
        self._running = True
        self._reply_channel = reply_channel
        self._publish_interval = 1.0 / frequency
        self._data = 0

    def run(self):
        while self._running:
           self._reply_channel.send({'text': self._data})
           self._data += 1
           time.sleep(self._publish_interval)

    def stop(self):
        self._running = False

publishers = {}

def ws_connect(message):
    message.reply_channel.send({'accept': True})
    publisher = Publisher(reply_channel=message.reply_channel)
    publisher.start()
    publishers[message.reply_channel] = publisher

def ws_disconnect(message):
    publisher = publishers[message.reply_channel]
    publisher.stop()
    del publishers[message.reply_channel]