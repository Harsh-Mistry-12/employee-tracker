# channels.py
from datetime import datetime
from channels.generic.websocket import WebsocketConsumer
import subprocess
import json

today = datetime.now()
formatted_date = today.strftime('%Y%m%d')

# class LiveLogConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()

class LogConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self):
        # Continuously read the log file and send updates to the client
        with open(f'C:\\Users\\Admin\\Documents\\HARSH\\clg_project\\tracker\\track\\track-log\\192.168.56.1\\Admin\\{formatted_date}\\history', 'r') as f:
            while True:
                line = f.readline().strip()
                if line:
                    log_data = json.loads(line)
                    self.send(text_data=json.dumps({
                    'log_content': log_data['content']
                    }))
                # if line:
                #     self.send(text_data=line.strip())