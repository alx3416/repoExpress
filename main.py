# hola mundo en python
import math

def myFunction():
    print("Hola mundo")


def getSquareArea(side):
    return side ** 2


def getCircleArea(radius):
    return math.pi * (radius ** 2)

myFunction()
print(getSquareArea(3))
print(getCircleArea(10))