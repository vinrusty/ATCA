import threading
from time import sleep
from random import choice

semaphore = threading.Semaphore(1)

def weather_condition():
    return choice([True, False])

def plane(plane_no):
    print(f'Plane {plane_no} is waiting\n')
    while semaphore._value <= 0 and weather_condition():
        pass
    semaphore.acquire()
    print(f"Plane {plane_no} has acquired runway\n")
    print(f'The plane {plane_no} is landing\n')
    sleep(2)
    semaphore.release()
    print(f"""Plane {plane_no} has finished landing, the runway is free\n""")

threads = []

for i in range(3):
    t = threading.Thread(target=plane, args=[i+1])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

