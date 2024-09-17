import json
from channels.generic.websocket import AsyncWebsocketConsumer

class RaspberryConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.device_id = self.scope['url_route']['kwargs']['device_id']
        self.group_name = f'device_{self.device_id}'
        
        # Add this WebSocket connection to the device's group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        response = data.get('response')

        await self.channel_layer.group_send(
            f"device_{self.device_id}",
            {
                'type': 'receive_response',  # Custom handler for the response
                'response': response         # Send back the response
            }
        )

    async def send_command(self, event):
        command = event['message']
        await self.send(text_data=json.dumps({
            'command': command
        }))

    async def receive_response(self, event):
        response = event['response']

        await self.send(text_data=json.dumps({
            'response': response
        }))
