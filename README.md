# Raspberry Pi Programs

## Overview

This repository contains a collection of Raspberry Pi programming examples developed using **Python**. The programs are designed for beginners as well as intermediate learners and cover GPIO interfacing, sensor integration, communication protocols, and embedded system applications.

These examples can be used for:

* Academic learning
* Laboratory experiments
* Embedded systems training
* IoT project development
* Raspberry Pi hardware interfacing

---

## Hardware Requirements

* Raspberry Pi 4 Model B (Recommended)
* MicroSD Card (16 GB or higher)
* Power Supply (5V, 3A)
* Breadboard
* Jumper Wires
* LEDs
* Push Buttons
* Resistors
* Buzzer
* 16×2 LCD Display
* 4×4 Matrix Keypad
* Servo Motor
* Relay Module
* Sensors (DHT11, Ultrasonic, PIR, etc.)

---

## Software Requirements

* Raspberry Pi OS
* Python 3
* VS Code (Optional)
* Thonny IDE (Optional)
* Terminal

### Required Python Libraries

```bash
sudo apt update
sudo apt install python3-pip

pip3 install RPi.GPIO
pip3 install gpiozero
pip3 install RPLCD
```

---

## Repository Structure

```
RaspberryPi_Programs/
│
├── GPIO/
│   ├── LED_Blink.py
│   ├── Push_Button.py
│   ├── Traffic_Light.py
│
├── LCD/
│   ├── LCD_16x2.py
│   ├── LCD_Custom_Characters.py
│
├── Keypad/
│   ├── Keypad_4x4.py
│   ├── Keypad_LCD.py
│
├── Sensors/
│   ├── Ultrasonic.py
│   ├── DHT11.py
│   ├── PIR.py
│
├── PWM/
│   ├── Servo_Control.py
│   ├── LED_Dimming.py
│
├── Communication/
│   ├── UART.py
│   ├── SPI.py
│   ├── I2C.py
│
└── README.md
```

---

## Topics Covered

### GPIO Programming

* LED Blinking
* Push Button
* Buzzer
* Traffic Light
* Relay Control

### Display Interfacing

* 16×2 LCD
* LCD in 4-bit Mode
* Custom Characters

### Keypad Interfacing

* 4×4 Matrix Keypad
* Password Entry
* Keypad with LCD

### Sensor Interfacing

* Ultrasonic Sensor (HC-SR04)
* DHT11 Temperature & Humidity Sensor
* PIR Motion Sensor
* LDR
* IR Sensor

### PWM Applications

* Servo Motor
* LED Brightness Control

### Communication Protocols

* UART
* SPI
* I²C

### IoT Applications

* ThingSpeak
* MQTT
* Firebase
* Web Server
* Wi-Fi Applications

---

## Running a Program

Navigate to the program directory:

```bash
cd RaspberryPi_Programs
```

Run the desired program:

```bash
python3 filename.py
```

Example:

```bash
python3 LED_Blink.py
```

---

## Learning Outcomes

After completing these programs, you will be able to:

* Configure Raspberry Pi GPIO pins
* Interface digital and analog peripherals
* Develop Python-based embedded applications
* Work with communication protocols
* Build IoT-based Raspberry Pi projects
* Design real-world embedded system applications

---

## Future Additions

* Camera Module
* Face Recognition
* OpenCV Projects
* MQTT Dashboard
* Firebase Integration
* Home Automation
* Smart Surveillance
* AI-Based Edge Computing
* Robotics Applications

---

## Contributing

Contributions are welcome. Feel free to add new Raspberry Pi examples, improve existing programs, or fix issues by submitting a pull request.

---

## License

This repository is intended for educational and training purposes. You are free to use and modify the programs for learning and non-commercial projects.

---

## Author

**Adhith D. John**
Regional Technical Head – Embedded
Embedded Systems | IoT | AI | Robotics | PCB Design

---

**Happy Learning and Happy Coding! 🚀**
