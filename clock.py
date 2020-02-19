"""
定义一个时钟,并可以转起来
"""


import time
import os


class Clock(object):
    def __init__(self, hour = 0,minute = 0,second = 0):
        self._hour = hour
        self._minute = minute
        self._second = second


    def run(self):
        self._second += 1
        if self._second == 60:
            self._minute += 1
            self._second = 0
            if self._minute == 60:
                self._hour += 1
                self._minute = 0
                if self._hour == 24:
                    self._hour = 0
        return "%d:%d:%d"%(self._hour,self._minute,self._second)

    def show(self):
        print(self.run())

def main():
    clock = Clock(23,59,50)
    while True:
        time.sleep(1)
        clock.show()


if __name__ == "__main__":
    main()

