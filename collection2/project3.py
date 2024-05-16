#know this isn't fully correct. I try :(

from pathlib import Path
import sys
from gpiozero import RGBLED
import time


CPU = open("/sys/class/thermal/thermal_zone0/temp",)
print(CPU.read(5))

LIGHT = RGBLED(red = 22, green = 27, blue = 17)

def loop(cpu_temp):
    while True:
        read_file = float(CPU.read(5)) /1000
        if 
        

def set_color(r, g, b):
    LIGHT.color = (1-r, 1-g, 1-b)
        
def destroy():
    LIGHT.close() #release rgbled
    

    
    

if __name__ == '__main__':   # Program entrance
    print ('Program is starting... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()          