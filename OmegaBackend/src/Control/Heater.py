class HeaterController:

    def __init__(self, maxWattage):
        self.isHeaterEnabled = False
        self.heaterOutput = 0.0
        self.maxWattage = maxWattage

    def setHeaterOutput(self, wattage):
        self.isHeaterEnabled = True
        self.heaterOutput = min(wattage, self.maxWattage)


    def disableHeater(self):
        self.heaterOutput = 0.0
        self.isHeaterEnabled = False
