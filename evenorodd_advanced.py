from microbit import *

# scrolling message:  A for easy mode, B for hard
# press A --> E, press B --> H
# Easy: 1.2 second to choose; Hard: 0.7 second to choose
# scrolling message:  A for even, B for odd
# generate random number 0 - 9
# press A --> even
# press B --> odd
# if correct --> happy face
# if wrong or time up --> angry face

import random

# mode: 1. easy --> 1200ms 2. hard --> 700ms
def mode(dif):
    if(dif == 2):
        return 700
    else:
        return 1200

# right --> happy face; wrong --> angry face
def happy():
    display.clear()
    display.show(Image.HAPPY)

def angry():
    display.clear()
    display.show(Image.ANGRY)

# timer: mode(dif) determines difficulty(speed)
# within time, right button activates right, vice versa
def process(rb, wb):
    right = False
    wrong = False
    difficulty = speed
    start = running_time()
    now = running_time()
    # timer. referenced:
    # https://github.com/martinohanlon/microbit-micropython/blob/master/examples/bopbit.py#L74
    while (now - start < difficulty):
        if (rb.is_pressed()):
            right = True
        elif (wb.is_pressed()):
            wrong = True
        now = running_time()
    # return: whether player is right or wrong
    if (right is True) and (wrong is False):
        return True
    else:
        return False

# define variables game and speed(here speed value doesn't matter).
game = False
speed = 1200
display.scroll("Even or Odd. A for Easy. B for Hard.")

# player must press a button to choose difficulty before game starts.
while game is False:
    if (button_a.was_pressed()):
        display.clear
        display.show("E")
        sleep(500)
        speed = mode(1)
        display.scroll("A for Even. B for Odd.")
        game = True
    elif (button_b.was_pressed()):
        display.clear
        display.show("H")
        sleep(500)
        speed = mode(2)
        display.scroll("A for Even, B for Odd.")
        game = True

# loop starts here.
while game is True:
    answer = False
    num = random.randint(0, 9)

    # even --> right button is a. odd --> right button is b
    if (num % 2 == 0):
        display.clear()
        display.show(num)
        answer = process(button_a, button_b)
    elif (num % 2 == 1):
        display.clear()
        display.show(num)
        answer = process(button_b, button_a)

    if (answer is True):
        happy()
    else:
        angry()
    sleep(1000)