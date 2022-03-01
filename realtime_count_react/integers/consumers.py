# import json 
# from time import sleep 
# import threading 

# from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
# from asgiref.sync import async_to_sync

# class WSConsumer(WebsocketConsumer):
#     def __init__(self):
#         super().__init__()
#         self._id = 0
#         self.e_stop = threading.Event()

#     def connect(self):
#         async_to_sync(self.channel_layer.group_add)('count_{}'.format(self._id), self.channel_name)
#         self.accept() 
#         async_to_sync(self.channel_layer.group_send)("count_{}".format(self._id), 
#                             {"type": "send_info", "text": "accepted from the server"})
        
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         print(">>>  ", message)

#         if message == 'start':
#             async_to_sync(self.channel_layer.group_send)("count_{}".format(self._id), 
#                             {"type": "start_training", "text": "start the training"})
#         elif message == 'stop':
#             async_to_sync(self.channel_layer.group_discard)("count_{}".format(self._id), self.channel_name)
#             self._id += 1
#             async_to_sync(self.channel_layer.group_add)('count_{}'.format(self._id), self.channel_name)
#             self.e_stop.set()
            
#     def send_info(self, message):
#         info = message['text']
#         self.send(json.dumps({'type': 'INFO', 'message': info}))
        
#     def start_training(self, message):
#         info = message['text']

#         def task():
#             cnt = 0
#             for i in range(5):
#                 self.send(json.dumps({'type': 'TRAIN', 'message': cnt}))
#                 print(cnt)

#                 cnt += 1

#                 if self.e_stop.is_set():
#                     self.e_stop.clear()
#                     break
#                 sleep(1) # 1s
#         t = threading.Thread(target=task)
#         t.start()


import json 
from time import sleep 
import threading 
import asyncio

from channels.generic.websocket import AsyncWebsocketConsumer

class WSConsumer(AsyncWebsocketConsumer):
    def __init__(self):
        super().__init__()
        self._id = 0
        self.e_stop = threading.Event()

    async def connect(self):
        await self.channel_layer.group_add('count_{}'.format(self._id), self.channel_name)
        await self.accept() 
        await self.channel_layer.group_send("count_{}".format(self._id), 
                            {"type": "send_info", "text": "accepted from the server"})

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(">>>  ", message)

        if message == 'start':
            await self.channel_layer.group_send("count_{}".format(self._id), 
                            {"type": "start_training", "text": "start the training"})
        elif message == 'stop':
            await self.channel_layer.group_discard("count_{}".format(self._id), self.channel_name)
            self._id += 1
            await self.channel_layer.group_add('count_{}'.format(self._id), self.channel_name)
            self.e_stop.set()
            
    async def send_info(self, message):
        info = message['text']
        print(info)
        await self.send(json.dumps({'type': 'INFO', 'message': info}))
        
    async def start_training(self, message):
        info = message['text']
        print(info)
        async def task():
            cnt = 0
            for i in range(5):
                await self.send(json.dumps({'type': 'TRAIN', 'message': cnt}))
                print(cnt)

                cnt += 1
                if self.e_stop.is_set():
                    self.e_stop.clear()
                    break
                sleep(1)

        def between_callback():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            loop.run_until_complete(task())
            loop.close()
        t = threading.Thread(target=between_callback)
        t.start()
            







