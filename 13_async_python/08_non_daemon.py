#  the deamon threads are background threads that automatically shut down when the main program exists those used for non-critical background tasks like login and monitoring

import threading
import time


def monnitor_tea_tem():
    while True:
        print(f"Monitoring tea temperature...")

t = threading.Thread(target=monnitor_tea_tem)
t.start()

print("Main program done")