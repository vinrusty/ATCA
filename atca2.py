import threading
from time import sleep
from random import choice

runway = threading.BoundedSemaphore(2)
runways = {
    "1": '',
    "2": ''
}

weather = choice([True, False])

def plane(plane_no):
    global weather
    if weather:
        if runways["1"] != '' and runways["2"] != '':
            print(f'Plane {plane_no} is waiting for both the runway\n')
        elif runways["1"] == '' and runways["2"] != '':
            print(f'Plane {plane_no} is waiting for the runway 1\n')
        elif runways["2"] == '' and runways["1"] != '':
            print(f'Plane {plane_no} is waiting for the runway 2\n')
        else:
            print(f'Plane {plane_no} is going into runway 1 since both the runways are free\n')
        runway.acquire()
        if runways["1"] == '' and runways["2"] == '':
            runways["1"] = plane_no
        elif runways["1"] == '' and runways["2"] != '':
            runways["1"] = plane_no
        elif runways["2"] == '' and runways["1"] != '':
            runways["2"] = plane_no
        a = list(runways.values()).index(plane_no)+1
        print(f"Plane {plane_no} has acquired the runway {a} and needs 10s seconds to land\n")
        weather = choice([True, False])
        sleep(10)
        print(f"""Plane {plane_no} has finished landing in runway {a} \n""")
        print(f"The runway {a} is free\n")
        runways[str(a)] = ''
        runway.release()
    else:
        print(f"The weather is terrible for plane {plane_no}")
        weather = choice([True, False])



threads = []

for i in range(3):
    t = threading.Thread(target=plane, args=[i+1])
    t.start()
    sleep(1)
    threads.append(t)

for thread in threads:
    thread.join()

