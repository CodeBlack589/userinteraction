import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ButtonClick(WebsocketConsumer):
    def connect(self):
        self.button_name=self.scope['url_route']['kwargs']['button_name']
        self.room_group_name='chat_%s' % self.button_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type":"chat_message",
                "message":"Button Clicked :" + self.button_name
            }
        )
        self.accept()

    def chat_message(self,event):
        message=event['message']

        self.send(text_data=json.dumps({
            'message':message
        }))
class Coordinate(WebsocketConsumer):
    def connect(self):
        self.x=self.scope['url_route']['kwargs']['x']
        self.y=self.scope['url_route']['kwargs']['y']
        self.room_group_name='chat_%s' % self.x

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type":"chat_message",
                "message":"x:" + self.x+"y:"+self.y
            }
        )
        self.accept()

    def chat_message(self,event):
        message=event['message']

        self.send(text_data=json.dumps({
            'message':message
        }))

class Right(WebsocketConsumer):       
    def connect(self):
        self.x=self.scope['url_route']['kwargs']['x']
        self.room_group_name='chat_%s' % self.x

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type":"chat_message",
                "message":"Right KEy press"
            }
        )
        self.accept()

    def chat_message(self,event):
        message=event['message']

        self.send(text_data=json.dumps({
            'message':message
        }))
 