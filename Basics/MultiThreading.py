from threading import Thread
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for j in range(10):
            print("HI")
            sleep(1)


f1 = Hello()

f2=Hi()

f1.start()
f2.start()