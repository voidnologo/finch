from collections import namedtuple
import sys
import time
import tty
import termios

from finch import Finch


class ReadChar():

    def __enter__(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)

    def __exit__(self, type, value, traceback):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)


rbot = Finch()

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


def show_data(action, left=None, right=None):
    left = left if left else speed.left
    right = right if right else speed.right
    print(f'{action:10}{left:>8.2f}{right:>8.2f}')


def faster():
    global speed
    left = min(speed.left + .1, 1.0)
    right = min(speed.right + .1, 1.0)
    speed = Speed(left, right)


def reset_speed():
    global speed
    speed = Speed(.5, .5)


def slower():
    global speed
    left = max(speed.left - .1, 0.0)
    right = max(speed.right - .1, 0.0)
    speed = Speed(left, right)


def stop():
    # show_data('# stop')
    rbot.led(*off)
    rbot.wheels(0, 0)


def delay():
    time.sleep(.1)


def left():
    show_data('left', left=-1*speed.left)
    rbot.led(*red)
    # rbot.wheels(-1 * speed.left, speed.right)
    rbot.wheels(-.4, .4)
    delay()
    # stop()


def right():
    show_data('right', right=-1*speed.right)
    rbot.led(*blue)
    # rbot.wheels(speed.left, -1 * speed.right)
    rbot.wheels(.4, -.4)
    delay()
    # stop()


def forward():
    show_data('forward')
    rbot.led(*green)
    rbot.wheels(speed.left, speed.right)
    delay()
    # stop()


def back():
    show_data('back')
    rbot.led(*orange)
    rbot.wheels(-1 * speed.left, -1 * speed.right)
    delay()
    # stop()


def null():
    # show_data('null')
    pass


commands = {
    'j': left,
    'l': right,
    'i': forward,
    'k': back,
    'f': faster,
    's': slower,
    'd': reset_speed,
    ' ': stop,
}


while True:
    inp = get_input().lower()
    commands.get(inp, null)()
    inp = ''
