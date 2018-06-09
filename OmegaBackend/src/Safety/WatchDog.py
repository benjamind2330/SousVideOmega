import time
import threading

class Watchdog (threading.Thread):

    def __init__(self, delay):
        threading.Thread.__init__(self)
        self.i = 0
        self.delay = delay

    def run(self):
        while (True):
            print("Running ... Looped " + str(self.i) + " times")
            self.i = self.i + 1
            time.sleep(self.delay)
