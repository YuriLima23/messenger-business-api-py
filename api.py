

from typing import Dict, Union

import requests

from .exceptions import SendingMessageFailedException
from .types import ApiRequestPayload, OutgoingTextPayload

class MessengerAPI:

    def __init__(self,  access_token, api_version: str = 'v16.0'):
        self.access_token = access_token
        self.base_url = f'https://graph.facebook.com/{api_version}/'

    def send_message_text(self, page_id: str, message):
        obj = {
            "recipient": {
                "id":  page_id,
            },
            "messaging_type": "RESPONSE",
            "message": {
                "text": message
            }
        }
        result = requests.post(self.base_url + f'/{page_id}/messages/access_token={self.access_token}', json=obj)

        return result
