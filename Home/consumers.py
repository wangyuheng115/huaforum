from channels.generic.websocket import WebsocketConsumer
from .models import ysof_comment
from django.db import IntegrityError
import datetime
import json
from asgiref.sync import async_to_sync

class ComentConsumer(WebsocketConsumer):
    # websocket建立连接时执行方法
    def connect(self):
        self.room_group_name = 'public'

        # 将当前频道加入频道组
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    # websocket断开时执行方法
    def disconnect(self, close_code):
        pass

    # 从websocket接收到消息时执行函数
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        content = text_data_json['content']
        sender = text_data_json['sender']
        try:
            cleaned_content = content.strip()
            if cleaned_content != '':
                cleaned_content = ysof_comment(content=cleaned_content)
                cleaned_content.save()
                comment_text = cleaned_content.content
                comment_time = datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')
                # 广播评论给所有已连接的客户端
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'chat_comment',
                        'content': comment_text,
                        'time': comment_time,
                        'messagge': '评论发布成功',
                        'sender': sender
                    })
            else:
                self.send(text_data=json.dumps({
                    'type': 'chat_comment',
                    'sender': sender,
                    'message': '评论不能为空或只包含空格！'
                }))
        except IntegrityError:
            self.send(text_data=json.dumps({
                'type': 'chat_comment',
                'sender': sender,
                'message': '评论发布失败，请稍后再试。'
            }))



    def chat_comment(self, event):
        content = event["content"]
        time = event["time"]
        msg = event["messagge"]
        send = event["sender"]
        # 发送评论消息给客户端
        self.send(text_data=json.dumps({
            "content": content,
            "time": time,
            "messagge": msg,
            "sender": send,
        }))