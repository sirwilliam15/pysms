import pytest
import time

def test_att_control_center(att_manager):
    att_manager.add_device(
        iccid=''
    )
    sent_time = att_manager.send_sms('!rj')
    time.sleep(15)
    if len(att_manager.get_sms_history(from_date=sent_time)) == 0:
        pytest.fail('Did not get any messages')
    if len(att_manager.get_sms_history()) == 0:
        pytest.fail('Did not get any messages')


def test_twilio_client(twilio_manager):
    twilio_manager.add_device(
        phone=''
    )
    sent_time = twilio_manager.send_sms('hello there')
    time.sleep(15)
    if len(twilio_manager.get_sms_history(from_date=sent_time)) == 0:
        pytest.fail('Did not get any messages')
    if len(twilio_manager.get_sms_history()) == 0:
        pytest.fail('Did not get any messages')