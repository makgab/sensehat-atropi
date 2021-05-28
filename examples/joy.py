#from sense_hat import SenseHat
from sense_emu import SenseHat
import time

sense = SenseHat()
# sense.set_rotation(180)

while True:
    for x in sense.stick.get_events():
        if x.direction == 'up':
            sense.show_letter("D")
        elif x.direction == 'down':
            sense.show_letter("U")
        elif x.direction == 'left':
            sense.show_letter("R")
        elif x.direction == 'right':
            sense.show_letter("L")
        elif x.direction == 'middle':
            sense.show_letter("M")
