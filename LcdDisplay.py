## **3.16 \* 2 LCD Display**



pip3 install RPLCD



from RPLCD.gpio import CharLCD

import RPi.GPIO as GPIO

from time import sleep



lcd = CharLCD(cols=16, rows=2,

                 pin\_rs=7, pin\_e=8,

                 pins\_data=\[25,24,23,18],

                 numbering\_mode=GPIO.BCM)



lcd.write\_string("Hello Adam!")

sleep(3)

lcd.clear()

lcd.write\_string("Raspberry Pi 4")
