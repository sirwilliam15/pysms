import requests
from base64 import b64encode
from datetime import datetime

from .pysms import ApiRequestError, DeviceManager

class VerizonThingSpace(DeviceManager):
    base_url = 'https://staging.thingspace.verizon.com/api'
    service = 'verizon'
    
    def __init__(self, app_key, api_key, identifier='iccid'):
        super().__init__(identifier)
        self.account = account_id
        self.header = self._start_session(app_key, api_key)

    def _start_session(self, app_key, api_key):
        """
        """
        url = '%s/ts/v1/oauth2/token?grant_type=client_credentials'%self.base_url
        header = {
            'Authorization': 'Basic %s'%(b64encode('%s:%s'%(app_key, api_key).encode())).decode(),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        r = requests.post(url, headers=header)
        for c in r.cookies:
            token = c.value
        
    
    def send_sms(self, message, iccid=None, wait=False, timeout=10):
        """
        """
        if iccid is None: 
            iccid = self.current[self.identifier]
        elif type(iccid) == dict:
            iccid = [iccid[self.identifier]]
        elif type(iccid) == int or type(iccid) == str:
            iccid = [iccid]

        sent_time = datetime.now()
        response = requests.get('%s/m2m/v1/sms/%s/history'%(self.base_url, self.account)
                                    headers=self.header, params={
                                        'accountName': self.account,
                                        'kind': self.identifier.upper()
                                        'deviceIds': iccid,
                                        'smsMessage': message
                                    })
        return sent_time

        

    def get_sms_history(self, iccid=None, from_date=datetime.now().date(), all_msgs=False):
        """
        """
        if iccid is None:
            iccid = self.current

        
        response = requests.get('%s/m2m/v1/sms/%s/history'%(self.base_url, self.account)
                                    headers=self.header, params={
                                        'accountName': self.account,
                                    })
        
        return response['messages']
        