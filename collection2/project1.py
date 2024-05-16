import subprocess
from gpiozero import LED as LEDClass # Alias

import time


LED1 = LEDClass(17)  #offline (red)
LED2 = LEDClass(27)  #online (green)


def loop():
    global LED1, LED2
    while True:
        if is_internet_connected() == True:
            print ("internet is connected")
            LED1.on()
            LED2.off()
        else:
            print("internet is down")
            LED2.on()
            LED1.off()

        time.sleep(1)
        


def is_internet_connected():
    try:
    # Run the ping command with a timeout of 2 seconds and count 1 packet
        subprocess.check_output(['ping', '-c', '1', '-W', '2', 'www.google.com'])
        return True
    except subprocess.CalledProcessError:
        return False
    
def destroy():
    global LED1, LED2
    # Release resources
    LED1.close()
    LED2.close()
    

if __name__ == '__main__': #program start
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()

    