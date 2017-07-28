import time
from finch import Finch

rbot = Finch()


def forward(n):
    rbot.wheels(.5, .5)
    time.sleep(n)


def right(n):
    rbot.wheels(.5, -.5)
    time.sleep(n)


forward(2)
right(.6)
