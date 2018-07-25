from turtle import *

def simple_hexagon():
    for i in range(6):
        forward(100)
        left(60)

def polygon(side):
    for i in range(side):
        forward(100)
        left(360 / side)

polygon(10)