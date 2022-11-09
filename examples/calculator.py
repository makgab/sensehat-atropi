#!/usr/bin/python

#from sense_hat import SenseHat
from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

addiction = 0
deduction = 1
multiplication = 2
division = 3
operation = ("+", "-", "*", "/")

def input_number():
  number = 0
  sense.show_letter(str(number))
  end = False
  while not end:
    for event in sense.stick.get_events():
      if (event.direction == 'up') & (event.action == 'released'):
        if number != 9: number += 1
        sense.show_letter(str(number))
      if (event.direction == 'down') & (event.action == 'released'):
        if number != 0: number -= 1
        sense.show_letter(str(number))
      if (event.direction == 'middle') & (event.action == 'released'):
        end = True
        return number

def input_operation():
  global operation
  operpos = 0
  sense.show_letter(operation[operpos])
  end = False
  while not end:
    for event in sense.stick.get_events():
      if (event.direction == 'left') & (event.action == 'released'):
        if operpos != 0: operpos -= 1
        sense.show_letter(operation[operpos])
      if (event.direction == 'right') & (event.action == 'released'):
        if operpos != 3: operpos += 1
        sense.show_letter(operation[operpos])
      if (event.direction == 'middle') & (event.action == 'released'):
        end = True
        return operpos

while True:
  a = input_number()
  op = input_operation()
  b = input_number()
  if op == addiction:
    msg = str(a) + "+" + str(b) + "=" + str(a+b)
  elif op == deduction:
    msg = str(a) + "-" + str(b) + "=" + str(a-b)
  elif op == multiplication:
    msg = str(a) + "*" + str(b) + "=" + str(a*b)
  elif op == division:
    msg = str(a) + "/" + str(b) + "=" + str(round(a/b,2))
  sense.show_message(msg)
  sleep(1)

#programmed by: Csabi79