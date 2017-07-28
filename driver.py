from collections import namedtuple
import sys
import time
from read_char import ReadChar
# from finch import Finch


# rbot = Finch()

Speed = namedtuple('Speed', ['left', 'right'])
speed = Speed(.5, .5)


# LED COLORS
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)
off = (0, 0, 0)
on = (255, 255, 255)


def get_input():
    with ReadChar() as rc:
        char = rc.upper()
        if char in ['\x03']:
            sys.exit()
        return char


def show_data(action):
    print(f'{action:10}{speed.left:>8.2}{speed.right:>8.2}')


def faster():
    global speed
    left = speed.left + .1
    right = speed.right + .1
    if left > 1.0:
        left = 1.0
    if right > 1.0:
        right = 1.0
    speed = Speed(left, right)


def reset_speed():
    global speed
    speed = Speed(.5, .5)


def slower():
    global speed
    left = speed.left - .1
    right = speed.right - .1
    if left < 0.0:
        left = 0.0
    if right < 0.0:
        right = 0.0
    speed = Speed(left, right)


def stop():
    pass
    # show_data('stop')
    # rbot.wheels(0, 0)


def delay():
    time.sleep(.1)


def left():
    show_data('left')
    # rbot.led(*red)
    # rbot.wheels(-1 * speed.left, speed.right)
    delay()
    stop()


def right():
    show_data('right')
    # rbot.led(*blue)
    # rbot.wheels(speed.left, -1 * speed.right)
    delay()
    stop()


def forward():
    show_data('forward')
    # rbot.led(*green)
    # rbot.wheels(speed.left, speed.right)
    delay()
    stop()


def back():
    show_data('back')
    # rbot.led(*orange)
    # rbot.wheels(-1 * speed.left, -1 * speed.right)
    delay()
    stop()


def null():
    show_data('null')


commands = {
    'j': left,
    'l': right,
    'i': forward,
    'k': back,
    'f': faster,
    's': slower,
    'd': reset_speed,
}


while True:
    inp = get_input().lower()
    commands.get(inp, null)()
    inp = ''
