# API for the pump control

class PumpController:

    def __init__(self):
        # This will inevitably take some sort of hardware item or
        # similar interesting thing to allow it to control the pump
        # relay.
        self.isPumpEnabled = False

    def enablePump(self):
        self.isPumpEnabled = True

    def disablePump(self):
        self.isPumpEnabled = False
