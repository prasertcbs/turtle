from turtle import *

def simple_hexagon():
    for i in range(6):
        forward(100)
        left(360 / 6)

def simple_hexagon_2():
    '''
    สร้างตัวแปรสำหรับเก็บจำนวนด้าน
    '''
    side = 6
    for i in range(side):
        forward(100)
        left(360 / side)

def polygon(side):
    '''
    สร้างเป็นฟังก์ชัน
    '''
    for i in range(side):
        forward(100)
        left(360 / side)

def polygon2(side, pen_size=2):
    pensize(pen_size)
    polygon(side)

polygon2(10, 20)