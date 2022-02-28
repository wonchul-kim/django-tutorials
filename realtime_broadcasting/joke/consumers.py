from channels.generic.websocket import AsyncWebsocketConsumer 

class JokesConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        await self.channel_layer.group_add('jokes', self.channel_name)
                                        # group name, channel name(automatically assigned)
                                        # channel_layer is `first in first out` structure
        await self.accept() 

    # async def disconnect(self):
    #     await self.channel_layer.group_discard("jokes", self.channel_name)

    
    async def send_jokes(self, event):
        text_message = event['text']

        await self.send(text_message)

    
