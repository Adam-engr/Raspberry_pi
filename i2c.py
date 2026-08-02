# i2c

sudo raspi-config
# Interface Options → I2C → Enable

sudo apt update
sudo apt install i2c-tools python3-smbus
pip3 install RPLCD

i2cdetect -y 1  #to find lcd addrss

from RPLCD.i2c import CharLCD
from time import sleep

# Change address if needed (0x27 or 0x3F)
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)

try:
    while True:
        lcd.clear()
        lcd.write_string("Hello Adam")
        
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Raspberry Pi 4")
        
        sleep(3)

        lcd.clear()
        lcd.write_string("I2C LCD Working")
        
        sleep(2)

except KeyboardInterrupt:
    lcd.clear()