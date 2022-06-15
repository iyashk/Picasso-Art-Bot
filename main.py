import RPi.GPIO as GPIO
import curses
from time import sleep

en = 25
in1 = 23
in2 = 24
en1 = 17
in3 = 22
in4 = 27
temp1 = 1

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)

GPIO.setup(en1, GPIO.OUT)
GPIO.setup(in1, GPIO.LOW)
GPIO.setup(in2, GPIO.LOW)
GPIO.setup(in3, GPIO.LOW)
GPIO.setup(in4, GPIO.LOW)

p1 = GPIO.PWM(en, 1000)
p2 = GPIO.PWM(en1, 1000)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)

p1.start(25)
p2.start(25)
print("working")

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
GPIO.output(in2, GPIO.LOW)


def forward():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)


def backward():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)


def right():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)


def left():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)


def back_right():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)


def back_left():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)


def brake():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)


try:
    while True:
        char = screen.getch()
        if char == ord('t'):
            print("triangle")
            right()
            sleep(0.66)
            brake()
            # sleep(0.5)
            forward()
            sleep(1)
            brake()
            right()
            sleep(3.33)
            brake()
            forward()
            sleep(1)
            brake()
            right()
            sleep(3.33)
            brake()
            forward()
            sleep(1)
            brake()
        if char == ord('r'):
            print("rectangle")
            forward()
            sleep(0.5)
            brake()
            right()
            sleep(1)
            brake()
            forward()
            sleep(1)
            brake()
            right()
            sleep(1)
            brake()
            forward()
            sleep(0.5)
            brake()
            right()
            sleep(1)
            brake()
            forward()
            sleep(1)
            brake()
        if char == ord('c'):
            print("circle")
            right()
            sleep(4)
            brake()
        if char == ord('s'):
            print("square")
            forward()
            sleep(1)
            brake()
            right()
            sleep(1)
            brake()
            forward()
            sleep(1)
            brake()
            right()
            sleep(1)
            brake()
            forward()
            sleep(1)
            brake()
            right()
            sleep(1)
            brake()
            forward()
            sleep(1)
            brake()
        if char == ord('p'):
            print("pentagon")
            left()
            sleep(0.2)
            brake()
            forward()
            sleep(0.5)
            brake()

            right()
            sleep(2.8)
            brake()
            forward()
            sleep(0.5)
            brake()

            right()
            sleep(2.8)
            brake()
            forward()
            sleep(0.5)
            brake()

            right()
            sleep(2.8)
            brake()
            forward()
            sleep(0.5)
            brake()

            right()
            sleep(2.8)
            brake()
            forward()
            sleep(0.5)
            brake()

finally:
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
    GPIO.cleanup()
