import json 
from time import sleep 

from channels.generic.websocket import WebsocketConsumer

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept() 

        cnt = 0
        for i in range(100):
            self.send(json.dumps({'message': cnt}))

            cnt += 1
            sleep(1) # 1s
