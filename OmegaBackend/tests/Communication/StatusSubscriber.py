import os, sys, zmq
sys.path.append(os.path.join(os.path.dirname(__file__), "../../src/Communication"))

print ("Adding path: " + os.path.join(os.path.dirname(__file__), "../../src/Communication"))

from Messages import Status_pb2


#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting status updates from the sous vide…")
socket.connect("tcp://localhost:5556")

stat_filter = ""

socket.setsockopt_string(zmq.SUBSCRIBE, stat_filter)

while (True):
    packet_content = socket.recv()
    packet = Status_pb2.Status()
    packet.ParseFromString(packet_content)
    print ("Current Temp " + str(packet.temperature))
