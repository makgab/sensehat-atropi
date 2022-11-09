#!/usr/bin/python

#from sense_hat import SenseHat
from sense_emu import SenseHat

from time import sleep
import random

sense = SenseHat()

#clearing
sense.clear()
sleep(1)

#initializing
left = 0
up = 1
right = 2
down = 3
growing = True
backcolor = (0, 0, 0)
headcolor = (204, 153, 102)
bodycolor = (255, 255, 255)
bodycolor2 = (248, 252, 248)
foodcolor1 = (255, 255, 0)
foodcolor2 = (51, 102, 255)
foodcolor3 = (46, 184, 46)
snakelength = 1
waittime = 0.8
end = False

#functions
def drawing():
  global snake
  global growing
  global snakelength
  if not growing:
    sense.set_pixel(snake[-2], snake[-1], backcolor[0], backcolor[1], backcolor[2])
    snake.pop()
    snake.pop()
  else: snakelength += 1
  sense.set_pixel(snake[0], snake[1], headcolor[0], headcolor[1], headcolor[2])
  sense.set_pixel(snake[2], snake[3], bodycolor[0], bodycolor[1], bodycolor[2])

def going():
  global snake
  global growing
  global direction
  global nextdirection
  global snakelength
  global end
  def go_left():
    global snake
    global direction
    global nextdirection
    newposx = snake[0]-1
    if newposx == -1:
      newposx = 7
    newposy = snake[1]
    snake.insert(0,newposy)
    snake.insert(0,newposx)
    direction = left
    nextdirection = up
  def go_right():
    global snake
    global direction
    global nextdirection
    newposx = snake[0]+1
    if newposx == 8:
      newposx = 0
    newposy = snake[1]
    snake.insert(0,newposy)
    snake.insert(0,newposx)
    direction = right
    nextdirection = up
  def go_up():
    global snake
    global direction
    global nextdirection
    newposx = snake[0]
    newposy = snake[1]-1
    if newposy == -1:
      newposy = 7
    snake.insert(0,newposy)
    snake.insert(0,newposx)
    direction = up
    nextdirection = up
  def go_down():
    global snake
    global direction
    global nextdirection
    newposx = snake[0]
    newposy = snake[1]+1
    if newposy == 8:
      newposy = 0
    snake.insert(0,newposy)
    snake.insert(0,newposx)
    direction = down
    nextdirection = up
  #--------------------------    
  if direction == up:
    if nextdirection == left: go_left()
    elif nextdirection == right: go_right()
    else: go_up()
  elif direction == down:
    if nextdirection == left: go_right()
    elif nextdirection == right: go_left()
    else: go_down()
  elif direction == left:
    if nextdirection == left: go_down()
    elif nextdirection == right: go_up()
    else: go_left()
  elif direction == right:
    if nextdirection == left: go_up()
    elif nextdirection == right: go_down()
    else: go_right()
  #checking next pixel
  nextpixel = sense.get_pixel(snake[0], snake[1])
  if nextpixel == list(backcolor): drawing()
  elif nextpixel == list(bodycolor2):
    if (snake[0] == snake[-2]) & (snake[1] == snake[-1]): drawing()
    else:
      sense.set_pixel(snake[0], snake[1], headcolor[0], headcolor[1], headcolor[2])
      sense.set_pixel(snake[2], snake[3], bodycolor[0], bodycolor[1], bodycolor[2])
      sleep(0.4)
      for i in range(4):
        sense.set_pixel(snake[0], snake[1], 255, 0, 0)
        sleep(0.4)
        sense.set_pixel(snake[0], snake[1], headcolor[0], headcolor[1], headcolor[2])
        sleep(0.4)
      end = True
  else: #if nextpixel = food
    growing = True
    drawing()
    growing = False
    if snakelength == 64:
      sleep(1.4)
      end = True
    else: food_init()
  
def snake_init():
  global snake
  global direction
  global nextdirection
  x = random.randint(0,7)
  y = random.randint(0,7)
  snake = [x, y]
  direction = random.randint(0,3)
  nextdirection = random.randint(0,3)
  going()
  nextdirection = random.randint(0,3)
  going()

def food_init():
  global snakelength
  ended = False
  while not ended:
    x = random.randint(0,7)
    y = random.randint(0,7)
    foodpixel = (x, y)
    if snakelength < 63:
      if sense.get_pixel(x, y) == list(backcolor):
        randomcolor = random.randint(0,2)
        if randomcolor == 0: sense.set_pixel(x, y, foodcolor1[0], foodcolor1[1], foodcolor1[2])
        elif randomcolor == 1: sense.set_pixel(x, y, foodcolor2[0], foodcolor2[1], foodcolor2[2])
        else: sense.set_pixel(x, y, foodcolor3[0], foodcolor3[1], foodcolor3[2])
        ended = True
    else: ended = True

#main program
print("navigation: joystick left & right")
print("speed up & down: joystick up & down")
print("pause: joystick middle")
snake_init()
food_init()
food_init()
growing = False
while not end:
  for event in sense.stick.get_events():
    if (event.direction == 'left') & (event.action == 'pressed'):
      nextdirection = left
    elif (event.direction == 'right') & (event.action == 'pressed'):
      nextdirection = right
    elif (event.direction == 'up') & (event.action == 'pressed'):
      if waittime > 0.3: waittime -= 0.1
    elif (event.direction == 'down') & (event.action == 'pressed'):
      if waittime < 1: waittime += 0.1
    elif (event.direction == 'middle') & (event.action == 'pressed'):
      exitpause = False
      while not exitpause:
        for event in sense.stick.get_events():
          if (event.direction == 'middle') & (event.action == 'pressed'):
            exitpause = True
  going()
  sleep(waittime)

sense.clear()
sleep(0.8)
if snakelength == 64: sense.show_message("EXCELLENT!", text_colour=[255, 255, 0])
elif snakelength > 32: sense.show_message("WELL DONE!", text_colour=[255, 255, 0])
else: sense.show_message("BYE!", text_colour=[255, 255, 0])

#programmed by: Csabi79