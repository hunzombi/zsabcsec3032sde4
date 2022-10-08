from threading import Thread
import threading
import time

class Monke(object):
    def __init__(self):
        self.free = True
        self.time = 1


consusmers = 50
wait = 0

def shop():
    global staff
    while len(staff) == 0:
        time.sleep(Monke().time)
    try:
        m = staff.pop()
        time.sleep(m.time)
        staff.append(Monke())
        print("done")
        consumers -= 1
    except:
        shop()
    finally:
        return None

def timer():
    time.sleep(1)
    wait += 1


consumers = 50
staff = [Monke(), Monke(), Monke(), Monke()]

for i in range(consumers):
    th = Thread(target=shop, args=())
    th.start()
    th.join()

a = Thread(target=timer, args=())
th.join()
a.join()

print(wait)