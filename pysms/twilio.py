import requests
import twilio
from base64 import b64encode
from datetime import datetime
from twilio.base.exceptions import TwilioRestException

from .pysms import ApiRequestError, DeviceManager

class Twilio(DeviceManager):
    
    def __init__(self, api_key, account_id):
        super().__init__()
        self.client = twilio.rest.Client(account_id, api_key)

    def send_sms(self, message, phone=None, wait=False, timeout=10):
        """
        """
        if phone is None:
            phone = self.current
        try:
            message = self.client.messages.create(
                to=phone,
                body=message
            )
        except TwilioRestException as e:
            raise ApiRequestError(e)

    def get_sms_history(self, iccid=None, from_date=datetime.now().date(), all_msgs=False):
        """
        """
        pass