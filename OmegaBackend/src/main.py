import os, sys, zmq
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))
from Safety import WatchDog
from Communication import PublishInfo

net_context = zmq.Context()


#watchdog = WatchDog.Watchdog(2)
#watchdog.start()
#watchdog.join()

publisher = PublishInfo.Publisher(1, net_context)
publisher.start()
publisher.join()
