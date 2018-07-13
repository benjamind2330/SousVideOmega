class HeaterController:

    def __init__(self):
        self.isHeaterEnabled = False
        self.heaterOutput = 0.0

    def setHeaterOutput(self, wattage):
        self.isHeaterEnabled = True
        self.heaterOutput = wattage

    def disableHeater(self):
        self.heaterOutput = 0.0
        self.isHeaterEnabled = False
