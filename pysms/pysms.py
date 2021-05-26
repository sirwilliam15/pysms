from threading import Thread
from multiprocessing import Pool
from datetime import datetime

def join_threads(threads):
    for t in threads:
        t.join()

class ApiRequestError(Exception):
    def __init__(self, message):
        super().__init__(message)

class DeviceManager():
    def __init__(self):
        self.current = None
        self.devices = []

    def add_device(self, iccid):
        self.devices.append(iccid)

    def switch_device(self, iccid):
        self.current = iccid
        if iccid not in self.devices:
            self.add_device(iccid)

    def send_all(self, message):
        _threads = []
        for device in self.devices:
            t = Thread(target=self.send_sms, args=(message, device))
            _threads.append(t)
            t.start()

        t = Thread(target=join_threads, args=(_threads, ))
        t.start()

    def read_all(self, time=datetime.now().date()):
        _times = [time] * len(self.devices)
        _threads = []

        _history = Pool(self.get_sms_history, args=(self.devices, _times))

        sms_history = {}
        for dev, msg, in zip(self.devices, _history):
            sms_history[d] = msg

        return sms_history