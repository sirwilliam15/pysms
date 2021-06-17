import pytest

from configparser import ConfigParser
from pysms import *

conf = ConfigParser()
conf.read('config.ini')

@pytest.fixture(scope='module')
def att_manager():
    username = conf['ENV']['ATT Username']
    api_key = conf['ENV']['ATT API Key']
    account_id = conf['ENV']['ATT Account ID']
    return ATTControlCenter(username, api_key, account_id)

@pytest.fixture(scope='module')
def vzw_manager(app_key, api_key):
    return VerizonThingSpace(app_key, api_key)

@pytest.fixture(scope='module')
def twilio_manager():
    api_key = conf['ENV']['Twilio API Key']
    account_id = conf['ENV']['Twilio Account ID']
    phone = conf['ENV']['Twilio Phone Number']
    return TwilioClient(api_key, account_id, phone)