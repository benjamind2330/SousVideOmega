import time
import collections

def sign(x):
    if (x < 0):
        return -1
    else:
        return 1

class PIDController:

    def __init__(self, Kp, Ki, Kd, windupGaurd, derivativeWindow):
        self.Kp = Kp
        self.Ki = Ki
        self.integralWindupGaurd = windupGaurd
        self.Kd = Kd
        self.dWindowLength = derivativeWindow
        self.clear()

    def clear(self):
        self.setPoint = 0.0
        self.iValue = 0.0

        self.dValue = collections.deque(maxlen = self.dWindowLength)
        self.dWindowIndex = 0
        self.dWindowFull = False

        self.lastError = 0.0
        self.lastTime = time.time()


    def setTarget(self, setPoint):
        self.setPoint = setPoint

    def update(self, plantValue):
        error = self.setPoint - plantValue
        currentTime = time.time()
        deltaError = error - self.lastError
        deltaTime = currentTime - self.lastTime

        # derivate
        self.dValue.append((error, currentTime))
        if (len(self.dValue) != self.dWindowLength):
            dValueCurrent = 0
        else:
            dValueCurrent = (self.dValue[-1][0] - self.dValue[0][0]) / (self.dValue[-1][1] - self.dValue[0][1])

        # integrate

        #if the error sign flips reset the integral to prevent too much overshoot
        if (sign(error) != sign(self.lastError)):
            self.iValue = 0

        self.iValue += error * deltaTime
        if (self.integralWindupGaurd != 0):
            self.iValue = min(self.integralWindupGaurd, (max(-self.integralWindupGaurd, self.iValue)))

        # return the update dValue

        KpElement = error*self.Kp
        KdElement = dValueCurrent*self.Kd
        KiElement = self.iValue*self.Ki

        print ("error " + str(error) + " | Kp: " + str(KpElement) + " | Kd: " + str(KdElement) + " | Ki: " + str(KiElement))

        self.lastError = error
        self.lastTime = currentTime

        return (KpElement + KdElement + KiElement)
