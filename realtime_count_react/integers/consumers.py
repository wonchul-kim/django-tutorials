import json 
from time import sleep 

from channels.generic.websocket import WebsocketConsumer

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept() 

        self.send(json.dumps({"message": "accepted from the server"}))
        # cnt = 0
        # for i in range(100):
        #     self.send(json.dumps({'message': cnt}))

        #     cnt += 1
        #     sleep(1) # 1s

    def disconnect(self, close_code):
        pass 

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print(message)
