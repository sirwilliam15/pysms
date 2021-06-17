import requests
from base64 import b64encode
from datetime import datetime

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

from .pysms import ApiRequestError, DeviceManager

class TwilioClient(DeviceManager):
    
    def __init__(self, api_key, account_id, phone=None, identifier='phone'):
        super().__init__(identifier)
        self.client = Client(account_id, api_key)
        self.phone = phone

    def send_sms(self, message, phone=None, wait=False, timeout=10):
        """
        """
        if phone is None:
            phone = self.current
        try:
            message = self.client.messages.create(
                from_=self.phone,
                to=phone,
                body=message
            )
        except TwilioRestException as e:
            raise ApiRequestError(e)

        return message.date_created

    def get_sms_history(self, phone=None, from_date=datetime.now().date(), all_msgs=False, max_msgs=20):
        """
        """
        if phone is None:
            phone = self.current
        try:
            if all_msgs:
                messages = self.client.messages.list(
                    date_sent=from_date,
                    limit=max_msgs
                    )
            else:
                messages = self.client.messages.list(
                date_sent=from_date,
                to=self.phone,
                limit=max_msgs
                )
        except TwilioRestException as e:
            raise ApiRequestError(e)

        # sms_history = []
        # for msg in messages:
        #     if msg.to == self.phone or all_msgs:
        #         sms_history.append(msg)

        return sms_history