## **4.Keypad**



import RPi.GPIO as GPIO

import time



GPIO.setmode(GPIO.BCM)



rows = \[5,6,13,19]

cols = \[12,16,20,21]



keys = \[

    \['1','2','3','A'],

    \['4','5','6','B'],

    \['7','8','9','C'],

    \['\*','0','#','D']

]



for r in rows:

       GPIO.setup(r, GPIO.OUT)

       GPIO.output(r, 1)



for c in cols:

       GPIO.setup(c, GPIO.IN, pull\_up\_down=GPIO.PUD\_DOWN)



while True:

       for i, r in enumerate(rows):

           GPIO.output(r, 0)

           for j, c in enumerate(cols):

               if GPIO.input(c) == 1:

                   print("Key:", keys\[i]\[j])

                   time.sleep(0.3)

           GPIO.output(r, 1)
