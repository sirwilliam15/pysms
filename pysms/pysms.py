

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