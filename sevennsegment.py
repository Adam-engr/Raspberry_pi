## **2. Seven segment**



import RPi.GPIO as GPIO

import time



GPIO.setmode(GPIO.BCM)



segments = \[17,18,27,22,23,24,25]



for pin in segments:

       GPIO.setup(pin, GPIO.OUT)



digits = {

       '0':\[1,1,1,1,1,1,0],

       '1':\[0,1,1,0,0,0,0],

       '2':\[1,1,0,1,1,0,1],

       '3':\[1,1,1,1,0,0,1],

       '4':\[0,1,1,0,0,1,1],

       '5':\[1,0,1,1,0,1,1],

       '6':\[1,0,1,1,1,1,1],

       '7':\[1,1,1,0,0,0,0],

       '8':\[1,1,1,1,1,1,1],

       '9':\[1,1,1,1,0,1,1]

}



while True:

       for num in digits:

           for i in range(7):

               GPIO.output(segments\[i], digits\[num]\[i])

           time.sleep(1)