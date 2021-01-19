# SenseHAT - Astro-Pi
Raspberry Pi SenseHAT (Astro-Pi) module
# Sense HAT
Python module to control the Raspberry Pi Sense HAT used in the Astro Pi mission - an education outreach programme for UK schools sending code experiments to the International Space Station.

# Hardware
The Sense HAT features an 8x8 RGB LED matrix, a mini joystick and the following sensors:

Gyroscope
Accelerometer
Magnetometer
Temperature
Humidity
Barometric pressure

# Installation
To install the Sense HAT software, enter the following commands in a terminal:

* sudo apt-get update
* sudo apt-get install sense-hat
* sudo reboot

# Usage
Import the sense_hat module and instantiate a SenseHat object:

from sense_hat import SenseHat

sense = SenseHat()

# Documentation
Comprehensive documentation is available at https://pythonhosted.org/sense-hat
https://github.com/astro-pi/python-sense-hat
