from pathlib import Path
import sys
from gpiozero import LED
import time

HERE = Path(__file__).parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import *


LED1 = LED(17)  #blue
LED2 = LED(22)  #green
LED3 = LED(27)  #yellow
LED4 = LED(5)   #red
ADC = ADCDevice()



def setup():
    global ADC 
    if(ADC.detectI2C(0x48) and USING_GRAVITECH_ADC): 
        ADC = GravitechADC()
    elif(ADC.detectI2C(0x48)): # Detect the pcf8591.
        ADC = PCF8591()
    elif(ADC.detectI2C(0x4b)): # Detect the ads7830
        ADC = ADS7830()
    else:
        print("No correct I2C address found, \n"
            "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
            "Program Exit. \n")
        exit(-1)
        
def loop():
    global ADC, LED1, LED2, LED3, LED4
    while True:
        value = ADC.analogRead(0)   # read the ADC value of channel 0
        if 255/4 * 1 < value:
            LED1.on()
        else:
            LED1.off()
        if 255/4 * 2 < value:
            LED2.on()
        else:
            LED2.off()
        if 255/4 * 3 < value:
            LED3.on()
        else:
            LED3.off()
        if 255 * 0.9 <= value:
            LED4.on()
        else:
            LED4.off()
            
                
    #LED.value = value / 255.0   # Mapping to PWM duty cycle        
        voltage = value / 255.0 * 3.3
        print (f'ADC Value: {value} \tVoltage: {voltage:.2f} ')
        time.sleep(0.1)    
    
def destroy():
    global ADC, LED1, LED2, LED3, LED4
    ADC.close()
    LED1.close()
    LED2.close()
    LED3.close()
    LED4.close()
                
                
if __name__ == '__main__':   # Program entrance
    print ('Program is starting... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()          
        
    