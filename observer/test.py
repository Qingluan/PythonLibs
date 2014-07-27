from time import sleep
import time
from Observer import Observer
import sys

class Ticker(Observer):
    def dosome(self):
        while 1:
            sleep(1)
            self.changed()
            self.notify_observer(time.asctime())

class Text:
    def update(self,arg):
        sys.stdout.write("{}\r".format(arg))
        sys.stdout.flush()

if __name__ == "__main__":
    a = Ticker()
    tex = Text()
    a.add_observable(tex)
    a.dosome()