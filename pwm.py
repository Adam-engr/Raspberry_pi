## **7.PWM**



import RPi.GPIO as GPIO

import time



LED = 18



GPIO.setmode(GPIO.BCM)

GPIO.setup(LED, GPIO.OUT)



pwm = GPIO.PWM(LED, 1000)

pwm.start(0)



while True:

       for duty in range(0,101,5):

           pwm.ChangeDutyCycle(duty)

           time.sleep(0.1)
