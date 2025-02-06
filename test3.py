import RPi.GPIO as GPIO
from time import *

# Definicja pinów
L1 = 17
L2 = 27
B1 = 22

# Konfiguracja GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(B1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    Bstate = GPIO.input(B1)
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(L2, GPIO.LOW)

    if Bstate:
        GPIO.output(L2, GPIO.LOW)
        GPIO.output(L1, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(L1, GPIO.LOW)
        GPIO.output(L2, GPIO.HIGH)
        sleep(0.5)
