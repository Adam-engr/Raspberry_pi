## **8.motor interface (Servo)**



import RPi.GPIO as GPIO

import time



servo = 18



GPIO.setmode(GPIO.BCM)

GPIO.setup(servo, GPIO.OUT)



pwm = GPIO.PWM(servo, 50)

pwm.start(0)



def set\_angle(angle):

       duty = 2 + (angle / 18)

       GPIO.output(servo, True)

       pwm.ChangeDutyCycle(duty)

       time.sleep(0.5)

       GPIO.output(servo, False)



while True:

       set\_angle(0)

       time.sleep(1)

       set\_angle(90)

       time.sleep(1)

       set\_angle(180)

       time.sleep(1)
