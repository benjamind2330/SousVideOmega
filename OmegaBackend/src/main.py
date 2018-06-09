import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))
from Safety import WatchDog

watchdog = WatchDog.Watchdog(2)
watchdog.start()

watchdog.join()
