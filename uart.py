# uart

sudo raspi-config
# Interface Options → Serial → Disable login shell, Enable serial port

pip3 install pyserial

import serial
import time

ser = serial.Serial(
    port='/dev/serial0',
    baudrate=9600,
    timeout=1
)

while True:
    ser.write(b'Hello Adam\n')
    time.sleep(1)

    if ser.in_waiting:
        data = ser.readline().decode('utf-8').strip()
        print("Received:", data)
