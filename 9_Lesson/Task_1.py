import time
from itertools import cycle

class TrafficLight:

    def __init__(self):
        self.itime = [7, 2, 5, 7]
        self._color = 'Красный'

    def state(self):
        return self._color

    def running(self):
        x = 0
        for i in cycle(range(len(self.itime))):
            if i == 1 or i == 3:self._color = 'Жёлтый'
            elif i == 2:self._color = 'Зелёный'
            else:self._color = 'Красный'
            print(self._color)
            time.sleep(self.itime[i])
            if x == 8:
                break
            x += 1

tr = TrafficLight()
tr.running()

tr2 = TrafficLight()
tr2.running()



