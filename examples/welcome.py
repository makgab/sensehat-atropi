#!/usr/bin/python

#from sense_hat import SenseHat
from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

print("Üdvözöllek! Én egy python nyelven megírt program vagyok.")
name = input("Gépeld be a nevedet és üsd le az Entert: ")
print("")
print("Köszi! Figyeld a 8x8-as SenseHat kijelzőt!")
print("")
sleep(3)
sense.show_message("Szia, "+name+"!", text_colour=[255, 255, 0])
sleep(2.4)
print("Jó, hogy itt vagy, "+name+"! Nézz körül a teremben!")
sleep(6)
for i in range(10): print("")
