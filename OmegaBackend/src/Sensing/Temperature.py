class TempretureSensor:

    def __init__(self, waterBathEmulator):
        self.waterBathEmulator = waterBathEmulator

    def getCurrentTemp(self):
        return self.waterBathEmulator.currentTemp
