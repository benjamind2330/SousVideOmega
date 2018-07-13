import os, sys, zmq, time
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))
from Safety import WatchDog
from Communication import PublishInfo
from Control import Heater
from Control import Pump
from Control import WaterBathEmulator
from Sensing import Temperature

net_context = zmq.Context()

WATER_AMOUNT = 10.0 #L
INITIAL_WATER_TEMP = 23.0 #DegC


heaterController = Heater.HeaterController()
pumpController = Pump.PumpController()
waterBathEm = WaterBathEmulator.WaterBathEmulator(WATER_AMOUNT, INITIAL_WATER_TEMP, heaterController, pumpController)
tempSensor = Temperature.TempretureSensor(waterBathEm)

waterBathEm.start()

#watchdog = WatchDog.Watchdog(2)
#watchdog.start()
#watchdog.join()

publisher = PublishInfo.Publisher(1, net_context, tempSensor)
publisher.start()

publisher.join()
waterBathEm.join()
