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
    def __init__(self, identifier):
        self.current = None
        self.identifier = identifier
        self.devices = {}

    def add_device(self, **kwargs):
        self.devices[kwargs[self.identifier]] = kwargs
        self.current = kwargs[self.identifier]

    def switch_device(self, id):
        try:
            self.current = self.devices[id]
        except KeyError:
            raise KeyError('Device {} not in added devices'.format(id))

    def send_all(self, message):
        if self.service == 'verizon':
            self.send_sms(message, [i[self.identifier] for i in self.devices])
            return
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
            sms_history[dev] = msg

        return sms_history