import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))
from Safety import WatchDog
from Communication import PublishInfo




#watchdog = WatchDog.Watchdog(2)
#watchdog.start()
#watchdog.join()

publisher = PublishInfo.Publisher(1)
publisher.start()
publisher.join()
