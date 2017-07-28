# import sys
import time
# from read_char import ReadChar
from finch import Finch

rbot = Finch()


# def get_input():
#     with ReadChar() as rc:
#         char = rc.upper()
#         if char in ['\x03']:
#             sys.exit()
#         return char


def stop():
    rbot.wheels(0, 0)


def left(n):
    print('left')
    rbot.led(255, 0, 0)
    rbot.wheels(-.5, .5)
    time.sleep(n)
    stop()


def left_90():
    print('left_90')
    rbot.led(255, 0, 0)
    rbot.wheels(-.5, .5)
    time.sleep(.6)
    stop()


def right(n):
    print('left')
    rbot.led(0, 0, 255)
    rbot.wheels(.5, -.5)
    time.sleep(n)
    stop()


def right_90():
    print('right_90')
    rbot.led(0, 0, 255)
    rbot.wheels(.5, -.5)
    time.sleep(.6)
    stop()


def forward(n):
    for _ in range(n):
        fwd()


def fwd():
    print('forward')
    rbot.led(0, 255, 0)
    rbot.wheels(.8, .89)
    time.sleep(.5)
    stop()


def back(n):
    for _ in range(n):
        bck()


def bck():
    print('back')
    rbot.led(0, 0, 0)
    rbot.wheels(-.75, -.75)
    time.sleep(.5)
    stop()


forward(4)
right(.3)
forward(5)
left(.24)
forward(2)
left(.15)
forward(1)
right(.4)
forward(5)
right(.4)
forward(5)
left_90()
forward(5)
left(.22)
forward(15)
right(.7)
forward(9)
left_90()
forward(9)
left_90()
forward(8)
right(3)

# while True:
#     i = input('>>>')

#     if i == 'j':
#         left()

#     if i == 'l':
#         right()

#     if i == 'i':
#         forward()

#     if i == 'k':
#         back()

#     if i == 'q':
#         break

#     time.sleep(.01)
#     i = ''
