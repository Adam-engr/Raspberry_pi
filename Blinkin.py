# Author : Adhith D John

# **1. led  Bliking**

import RPi.GPIO as GPIO

import time



GPIO.setmode(GPIO.BCM)

LED = 18



while True:

       GPIO.output(LED, True)

       time.sleep(1)

       GPIO.output(LED, False)

       time.sleep(1)