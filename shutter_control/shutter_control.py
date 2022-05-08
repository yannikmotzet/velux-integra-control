import RPi.GPIO as GPIO
import time

GPIO_PIN_OPEN = 2
GPIO_PIN_STOP = 3
GPIO_PIN_CLOSE = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN_OPEN, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(GPIO_PIN_STOP, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(GPIO_PIN_CLOSE, GPIO.OUT, initial=GPIO.HIGH)
time.sleep(0.2)

def shutter_event(pin, duration):
    #GPIO.output(GPIO_PIN_OPEN, GPIO.HIGH)
    #GPIO.output(GPIO_PIN_STOP, GPIO.HIGH)
    #GPIO.output(GPIO_PIN_CLOSE, GPIO.HIGH)
    #time.sleep(0.2)

    GPIO.output(pin, GPIO.LOW)
    time.sleep(duration)
    GPIO.output(pin, GPIO.HIGH)

    #GPIO.output(GPIO_PIN_VCC, GPIO.LOW)
    #GPIO.output(GPIO_PIN_OPEN, GPIO.LOW)
    #GPIO.output(GPIO_PIN_STOP, GPIO.LOW)
    #GPIO.output(GPIO_PIN_CLOSE, GPIO.LOW)
    GPIO.cleanup()

def shutter_close(duration=0.2):
    shutter_event(GPIO_PIN_CLOSE, duration)

def shutter_open(duration=0.2):
    shutter_event(GPIO_PIN_OPEN, duration)

def shutter_stop():
    shutter_event(GPIO_PIN_STOP, 0.2)
