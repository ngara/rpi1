#!/usr/bin/env python

import sys
import time

import RPi.GPIO as GPIO

pins = [3, 2, 4]


def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
    # GPIO.output(pin, False)


def turn_on(delay=.2):
    for pin in pins:
        if delay:
            time.sleep(delay)
        GPIO.output(pin, True)


def turn_off(delay=.2):
    for pin in pins:
        if delay:
            time.sleep(delay)
        GPIO.output(pin, False)


def clear():
    turn_off(0)


def set_color(_color):
    c = {"red": 3, "yellow": 2, "green": 4}
    clear()
    try:
        GPIO.output(c[_color], True)
    except:
        pass


def run():
    while True:
        time.sleep(1)
        print "On"
        turn_on()
        time.sleep(1)
        print "Off"
        turn_off()


def cleanup():
    GPIO.cleanup()


def usage():
    print """Usage:

%s <setup|clear|red|yellow|green|cleanup>
""" % __file__


if __name__=='__main__':
    setup()
    if len(sys.argv) < 2:
        try:
            clear()
            run()
        finally:
            cleanup()
    else:
        option = sys.argv[1]
        if option == "setup":
            clear()
        elif option == "cleanup":
            cleanup()
        elif option == "clear":
            clear()
        elif option == "red":
            set_color("red")
        elif option == "yellow":
            set_color("yellow")
        elif option == "green":
            set_color("green")
        else:
            print sys.argv[0], ": Argument not understood."
            usage()
#
