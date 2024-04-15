from gpiozero import LED as LEDClass, Button
from signal import pause
import time 

LED = LEDClass(17)  # define ledPin
BUTTON = Button(18)  # define buttonPin
isStrobing = False

def changeLedState():
    global isStrobing
    isStrobing = not isStrobing
    
   
    
def strobe():
    global LED, isStrobing
    while True:
        if isStrobing == True:
            LED.on()
            time.sleep(0.1)
            LED.off()
            time.sleep(0.1)
        

def destroy():
    global LED, BUTTON
    # Release resources
    LED.close()
    BUTTON.close()

if __name__ == "__main__":     # Program entrance
    print ("Program is starting...")
    try:
        # If the button gets pressed, call the function
        # This is an event
        BUTTON.when_pressed = changeLedState
        strobe()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()