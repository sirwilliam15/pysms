from base64 import b64encode
from pysms import ApiRequestError, DeviceManager


class ATT():
    pass

class ATTControlCenter(DeviceManager):
    base_url = 'https://api-iotdevice.att.com/rws/api/v1'

    def __init__(self, username, api_key, account_id):
        # TODO
        super(DeviceManager).__init__()
        self.account = account_id
        self.header = {
            'Authorization': 'Basic %s'%(b64encode('%s:%s'%(username, api_key).encode())).decode(),
            'Content-Type': 'application/json'
        }

    def send_sms(self, message, iccid=self.current, wait=False, timeout=10):
    """
        Sends SMS to Registered Device\n
        Arguments
        ---------
        - Message : str
        - Wait for message to Deliver : bool
        - Timeout : int
    """
    try:
        response = requests.post('%s/devices/%d/smsMessages'%(atturl, int(iccid)),
                                    headers=attheader, data=json.dumps({'messageText': message}).encode('utf-8'))
        data = response.json()
        smsid = data['smsMessageId']

        if wait:
            for i in range(0, timeout, 3):
                time.sleep(3)
                status = self.get_sms_details(smsid)
                if status['status'] == 'Delivered':
                    break
        else:
            time.sleep(3)
            status = self.get_sms_details(smsid)
        return datetime.datetime.strptime(status['dateSent'], '%Y-%m-%d %H:%M:%S.%f%z')
    except KeyError:
        try:
            raise ApiRequestError(data['errorMessage'])
        except KeyError:
            raise ApiRequestError(data['response'])

    def get_sim_status(self, iccid=self.current):
        """
        Requests and checks if the device's SIM is in a Data Session
        """
        try:
            response = requests.get('%s/devices/%d/sessionInfo'%(atturl, int(iccid)),
                                        headers=attheader, params={'iccid': int(iccid)})
            data = response.json()
            try:
                sessionEnd = datetime.datetime.strptime(data['dateSessionEnded'], '%Y-%m-%d %H:%M:%S.%f%z')
            except TypeError:
                sessionEnd = None
            sessionStart = datetime.datetime.strptime(data['dateSessionStarted'], '%Y-%m-%d %H:%M:%S.%f%z')

            if sessionEnd is None:
                return 'In Session: %s'%data['dateSessionStarted']
            elif sessionStart > sessionEnd:
                return 'In Session: %s'%data['dateSessionStarted']
            else:
                return 'Last Session: %s'%data['dateSessionEnded']
        except KeyError:
            return data['errorMessage']

    def get_sms_details(smsid):

        parameters = {
            'smsMsgId':smsid,
        }

        url = '%s/smsMessages/%d'%(base_url, smsid)
        response = requests.get(url, headers=auth_head, params=parameters)
        return response.json()

    def get_sms_history(self, iccid=self.current, from_date=datetime.datetime.now().date(), all_msgs=False):
        """
        Requests and returns array of SMS history
        If all_msgs is True, return will include sent messages\n
        Arguments
        ---------
        - From Date : datetime
        - All Messages : bool
        Examples
        --------
        | ${msgs}= | Get SMS History | # Get Messages from Today | | |
        | ${msgs}= | Get SMS History | 1/1/2021 | all_msgs=${TRUE} | # Gets all messages from 1/1 |
        """
        time = from_date.strftime('%Y-%m-%dT%H:%M:%S%z')

        parameters = {
            'accountID': self.account, 
            'iccid': int(iccid), 
            'fromDate': time
            }
        response = requests.get('%s/smsMessages'%atturl, headers=attheader, params=parameters)
        data = response.json()['smsMsgIds']

        sms_history = []
        for smsid in data:
            response = self.get_sms_details(smsid)
            if r['sentTo'] == 'Server' or all_msgs:
                sms_history.append(r)

        return sms_history