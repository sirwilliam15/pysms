from threading import Thread

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