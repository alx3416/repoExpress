# hola mundo en python
import math

def myFunction():
    print("Hola mundo")


def getSquareArea(side):
    return side ** 2


def getCircleArea(radius):
    return math.pi * (radius ** 2)


def getTriangleArea(side1, side2):
    return (side1 * side2) / 2.0


myFunction()
print(getSquareArea(3))
print(getCircleArea(20))
print(getTriangleArea(5, 7))