import requests
from base64 import b64encode
from datetime import datetime

from .pysms import ApiRequestError, DeviceManager

class VerizonThingSpace(DeviceManager):
    base_url = 'https://staging.thingspace.verizon.com/api/'
    
    def __init__(self, app_key, api_key):
        super().__init__()
        self.account = account_id
        self.header = self._start_session(app_key, api_key)

    def _start_session(self, app_key, api_key):
        """
        """
        url = '%s/ts/v1/oauth2/token?grant_type=client_credentials'%base_url
        header = {
            'Authorization': 'Basic %s'%(b64encode('%s:%s'%(app_key, api_key).encode())).decode(),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        r = requests.post(url, headers=header)
        for c in r.cookies:
            token = c.value
        
    
    def send_sms(self, message, phone=None, wait=False, timeout=10):
        """
        """
        if phone is None:
            phone = self.current

    def get_sms_history(self, phone=None, from_date=datetime.now().date(), all_msgs=False):
        """
        """
        if iccid is None:
            iccid = self.current