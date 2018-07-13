import threading
import time
import zmq
from Communication.Messages import Status_pb2



class Publisher (threading.Thread):

    STATUS_TOPIC_NAME = "SV_Stat"

    def __init__(self, rate, context, tempretureSensor):
        threading.Thread.__init__(self)
        self.rate = rate;
        self.statusSocket = context.socket(zmq.PUB)
        self.statusSocket.bind("tcp://*:5556")
        self.tempretureSensor = tempretureSensor

    def generateStatusMessage(self):
        status = Status_pb2.Status()
        status.temperature = self.tempretureSensor.getCurrentTemp()
        return status

    def run(self):
        while (True):
            start = time.time()
            status = self.generateStatusMessage();
            #print("%s %s" % (self.STATUS_TOPIC_NAME, status.SerializeToString()))
            self.statusSocket.send(status.SerializeToString())
            time.sleep(max(1.0/self.rate - (time.time() - start), 0))
