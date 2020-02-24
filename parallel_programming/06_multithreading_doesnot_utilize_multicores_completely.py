# cpython runs only one thread at a given time

import os
import threading

def cpu_cycle_waster():
    while True:
        pass


print("\nprocess id : ", os.getpid())
print("thread count : ", threading.active_count())

for thread in threading.enumerate():
    print(thread)

print('\n starting 2 cpu wasters')
for i in range(2):
    threading.Thread(target=cpu_cycle_waster).start()

print("\nprocess id : ", os.getpid())
print("thread count : ", threading.active_count())

for thread in threading.enumerate():
    print(thread)