# import json 
# from time import sleep 

# from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
# from asgiref.sync import async_to_sync 

# class WSConsumer(WebsocketConsumer):
#     def connect(self):
#         async_to_sync(self.channel_layer.group_add)('count', self.channel_name)
#         self.accept() 

#         self.send(json.dumps({"message": "accepted from the server"}))
        
#         # cnt = 0
#         # for i in range(100):
#         #     await self.send_data()#json.dumps({'message': cnt}))
#         #     print(cnt)

#         #     cnt += 1

#         #     sleep(1) # 1s

#     def disconnect(self, close_code):
#         async_to_sync(self.channel_layer.group_discard)('count', self.channel_name)

#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         print(message)

#         if message == 'start':
#             async_to_sync(self.channel_layer.group_send)("count", {"type": "send_data", 'text': 'start'})
#         elif message == 'stop':
#             async_to_sync(self.channel_layer.group_discard)('count', self.channel_name)

#     def send_data(self, message):
#         print("send_data: ", message)
#         cnt = 0
#         for i in range(100):
#             self.send(json.dumps({'message': cnt}))
#             print(cnt)

#             cnt += 1


#             sleep(1) # 1s


##############################################################################################

import json 
from time import sleep 

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync 

class WSConsumer(AsyncWebsocketConsumer):
    def __init__(self):
        super(WSConsumer, self).__init__()
        self.cnt = 0

    async def connect(self):
        await self.channel_layer.group_add('count', self.channel_name)
        await self.accept() 

        await self.send(json.dumps({"message": "accepted from the server"}))
        
        # cnt = 0
        # for i in range(100):
        #     await self.send(json.dumps({'message': cnt}))
        #     print(cnt)

        #     cnt += 1

        #     sleep(1) # 1s

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('count', self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)

        if message == 'start':
            await self.channel_layer.group_send("count", {"type": "send_data", 'text': self.cnt})
            self.cnt += 1
        elif message == 'stop':
            await self.channel_layer.group_discard('count', self.channel_name)

    # async def send_data(self, message):
    #     print("send_data: ", message)
    #     cnt = 0
    #     for i in range(100):
    #         await self.send(json.dumps({'message': cnt}))
    #         print(cnt)

    #         cnt += 1


    #         sleep(1) # 1s

    async def send_data(self, message):
        message = message['text']
        print("send_data: ", message)
        await self.send(json.dumps({'message': message}))

##############################################################################################


# import json 
# from time import sleep 

# from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
# from asgiref.sync import sync_to_async

# class WSConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept() 
#         self.send(json.dumps({"message": "accepted from the server"}))
        
#         cnt = 0
#         for i in range(100):
#             self.send(json.dumps({'message': cnt}))
#             print(cnt)

#             cnt += 1
#             sleep(1) # 1s

#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         print(">>>  ", message)

