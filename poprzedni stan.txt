import RPi.GPIO as GPIO
from time import sleep

LEDS = [26, 19]
BUTTONS = [21, 12]

GPIO.setmode(GPIO.BCM)

for button in BUTTONS:
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

for led in LEDS:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)

L1 = False
L2 = True

try:
    while True:
        B1 = GPIO.input(BUTTONS[0])
        B2 = GPIO.input(BUTTONS[1])

        if B1 == GPIO.HIGH and L2 == True:
            L1 = True
            L2 = False
        if B2 == GPIO.HIGH and L1 == True:
            L1 = False
            L2 = True

        GPIO.output(LEDS[0], GPIO.HIGH if L2 else GPIO.LOW)
        GPIO.output(LEDS[1], GPIO.HIGH if L1 else GPIO.LOW)

        sleep(0.2)

except KeyboardInterrupt:
    print("Przerywam program!")

finally:
    GPIO.cleanup()
