## **6.motor interface (stepper)**



import RPi.GPIO as GPIO

import time



pins = \[17,18,27,22]



GPIO.setmode(GPIO.BCM)

for pin in pins:

       GPIO.setup(pin, GPIO.OUT)



sequence = \[

    \[1,0,0,1],

    \[1,0,0,0],

    \[1,1,0,0],

    \[0,1,0,0],

    \[0,1,1,0],

    \[0,0,1,0],

    \[0,0,1,1],

    \[0,0,0,1]

]



while True:

       for step in sequence:

           for i in range(4):

               GPIO.output(pins\[i], step\[i])

           time.sleep(0.002)
