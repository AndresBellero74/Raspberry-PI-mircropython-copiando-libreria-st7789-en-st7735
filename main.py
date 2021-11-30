"""
Raspberry Pi Pico/MicroPython exercise
128x128 st7735 SPI LCD
using MicroPython library:
https://github.com/russhughes/st7789py_mpy
adapted to st7735 by FBELLSAN-Informatica

"""

import uos
import time
import machine
import st7735py as st7735
from fonts import vga2_8x8 as font1
from fonts import vga1_16x32 as font2
import random

#SPI(1) default pins
spi1_sck=2
spi1_mosi=3
spi1_miso=4     #not use
st7735_cs = 1
st7735_res = 7
st7735_dc  = 0
disp_width = 128
disp_height = 128
CENTER_Y = int(disp_width/2)
CENTER_X = int(disp_height/2)

print(uos.uname())
spi0 = machine.SPI(0, baudrate=20000000, polarity=0, phase=0, sck=machine.Pin(2), mosi=machine.Pin(3), miso=machine.Pin(4))
print(spi0)
display = st7735.ST7735(spi0, disp_width, disp_width,
                          cs=machine.Pin(st7735_cs, machine.Pin.OUT),
                          reset=machine.Pin(st7735_res, machine.Pin.OUT),
                          dc=machine.Pin(st7735_dc, machine.Pin.OUT),
                          rotation=0)
display.fill(st7735.color565(255, 0, 0))
display.text(font2, "Red", 10, 10)
time.sleep_ms(1000)
display.fill(st7735.color565(0, 255, 0))
display.text(font2, "Green", 10, 10)
time.sleep_ms(1000)
display.fill(st7735.color565(0, 0, 255))
display.text(font2, "Blue", 10, 10)
time.sleep_ms(1000)
for r in range(255):
    display.fill(st7735.color565(r, 0, 0))
    
r_width = disp_width-20
r_height = disp_height-20
for g in range(255):
    display.fill_rect(10, 10, r_width, r_height, st7735.color565(0, g, 0))
    
r_width = disp_width-40
r_height = disp_height-40
for b in range(255):
    display.fill_rect(20, 20, r_width, r_height, st7735.color565(0, 0, b))

for i in range(255, 0, -1):
    display.fill(st7735.color565(i, i, i))

display.fill(st7735.BLACK)
display.text(font2, "Hello!", 10, 10)
display.text(font2, "RPi Pico", 10, 40)
display.text(font2, "MicroPython", 10, 70)
display.text(font1, "st7735 SPI 240*240 IPS", 10, 100)
display.text(font1, "https://github.com/", 10, 110)
display.text(font1, "russhughes/st7735py_mpy", 10, 120)

for i in range(5000):
    display.pixel(random.randint(0, disp_width),
          random.randint(0, disp_height),
          st7735.color565(random.getrandbits(8),random.getrandbits(8),random.getrandbits(8)))

# Helper function to draw a circle from a given position with a given radius
# This is an implementation of the midpoint circle algorithm,
# see https://en.wikipedia.org/wiki/Midpoint_circle_algorithm#C_example 
# for details
def draw_circle(xpos0, ypos0, rad, col=st7735.color565(255, 255, 255)):
    x = rad - 1
    y = 0
    dx = 1
    dy = 1
    err = dx - (rad << 1)
    while x >= y:
        display.pixel(xpos0 + x, ypos0 + y, col)
        display.pixel(xpos0 + y, ypos0 + x, col)
        display.pixel(xpos0 - y, ypos0 + x, col)
        display.pixel(xpos0 - x, ypos0 + y, col)
        display.pixel(xpos0 - x, ypos0 - y, col)
        display.pixel(xpos0 - y, ypos0 - x, col)
        display.pixel(xpos0 + y, ypos0 - x, col)
        display.pixel(xpos0 + x, ypos0 - y, col)
        if err <= 0:
            y += 1
            err += dy
            dy += 2
        if err > 0:
            x -= 1
            dx += 2
            err += dx - (rad << 1)
    
draw_circle(CENTER_X, CENTER_Y, 100)

for c in range(99):
    draw_circle(CENTER_X, CENTER_Y, c, st7735.color565(255, 0, 0))
    
for c in range(98):
    draw_circle(CENTER_X, CENTER_Y, c, st7735.color565(0, 255, 0))
    
for c in range(97):
    draw_circle(CENTER_X, CENTER_Y, c, st7735.color565(0, 0, 255))
    
print("- bye-")