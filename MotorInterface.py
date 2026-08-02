## **5.motor interface (dc)**



import RPi.GPIO as GPIO

import time



IN1 = 17

IN2 = 27

EN = 22



GPIO.setmode(GPIO.BCM)



GPIO.setup(IN1, GPIO.OUT)

GPIO.setup(IN2, GPIO.OUT)

GPIO.setup(EN, GPIO.OUT)



pwm = GPIO.PWM(EN, 1000)

pwm.start(50)



while True:

       GPIO.output(IN1, 1)

       GPIO.output(IN2, 0)

       print("Forward")

       time.sleep(3)



       GPIO.output(IN1, 0)

       GPIO.output(IN2, 1)

       print("Reverse")

       time.sleep(3)
