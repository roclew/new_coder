"""
计算平面内任意已知坐标的任意两点距离
"""

import math


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, x1=0, y1=0):
        return math.sqrt((self.x-x1)**2+(self.y-y1)**2)


def main():
    point1 = Point(5, 445)
    print(point1.x, point1.y)
    point1.y = 10
    print(point1.x, point1.y)
    print(point1.distance())


if __name__ == "__main__":
    main()

