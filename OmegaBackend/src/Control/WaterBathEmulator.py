import random
import threading
import time

# Q = mcΔT
# Therefore ΔT = Q/mc
# Q = J = Watts * S
# ΔT/s = Watts/mc
# Water has Specific heat (c) of 4.186
WATER_SPECIFIC_HEAT = 4.186


class WaterBathEmulator (threading.Thread):

    def __init__(self, waterAmount, initialTempreture, heatingElement, pumpControl, speedUpTime):
        threading.Thread.__init__(self)
        self.water_L = waterAmount #L
        self.currentTemp = initialTempreture #deg_C
        self.loopDelay = 1/speedUpTime #s
        self.heatingElement = heatingElement
        self.pumpControl = pumpControl
        random.seed()


    def getNoiseFactor(self):
        randFactor = random.uniform(-0.1, 0.1)
        # if the pump is on, less noise
        if (self.pumpControl.isPumpEnabled):
            randFactor = randFactor/2

        return randFactor + 1


    def run(self):
        while (True):
            self.currentTemp = self.currentTemp + \
                self.loopDelay * self.heatingElement.heaterOutput/(WATER_SPECIFIC_HEAT * (self.water_L * 1000)) * self.getNoiseFactor()

            time.sleep(self.loopDelay)
