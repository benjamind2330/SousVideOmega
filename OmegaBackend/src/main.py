import os, sys, zmq, time
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))
from Safety import WatchDog
from Communication import PublishInfo
from Control import Heater
from Control import Pump
from Control import WaterBathEmulator
from Sensing import Temperature
from Control import PIDController

net_context = zmq.Context()

WATER_AMOUNT = 10.0 #L
INITIAL_WATER_TEMP = 59 #Deg
MAX_HEATER_WATTAGE = 1500 #Watts
SPEED_UP_MULTIPLY = 20

heaterController = Heater.HeaterController(MAX_HEATER_WATTAGE)
pumpController = Pump.PumpController()
waterBathEm = WaterBathEmulator.WaterBathEmulator(WATER_AMOUNT, INITIAL_WATER_TEMP, heaterController, pumpController, SPEED_UP_MULTIPLY)
tempSensor = Temperature.TempretureSensor(waterBathEm)

waterBathEm.start()

#watchdog = WatchDog.Watchdog(2)
#watchdog.start()
#watchdog.join()

publisher = PublishInfo.Publisher(1, net_context, tempSensor)
publisher.start()

tempController = PIDController.PIDController(42, 0.1, 0.5, 100/0.01, 20)
tempController.setTarget(60)

while (True):
    # run the control loop
    outputValue = tempController.update(tempSensor.getCurrentTemp())
    if (outputValue <= 0):
        pumpController.disablePump()
        heaterController.disableHeater()
    else:
        pumpController.enablePump()
        heaterController.setHeaterOutput(outputValue)

    print("Current output value " + str(outputValue) + " | Heater value " + str(heaterController.heaterOutput))

    time.sleep(2)




publisher.join()
waterBathEm.join()
