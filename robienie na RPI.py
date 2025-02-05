import RPi.GPIO as GPIO
import time

# Konfiguracja pinów
BUTTONS = [17, 27, 22]  # Piny GPIO dla przycisków: B1, B2, B3
LEDS = [5, 6, 13, 19]  # Piny GPIO dla diod: L1, L2, L3, L4

# Ustawienie trybu numeracji i konfiguracja pinów
GPIO.setmode(GPIO.BCM)
for button in BUTTONS:
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
for led in LEDS:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)

try:
    while True:
        # Odczyt stanów przycisków
        B1 = GPIO.input(BUTTONS[0])
        B2 = GPIO.input(BUTTONS[1])
        B3 = GPIO.input(BUTTONS[2])

        # Logika dla L1
        if B1 == GPIO.HIGH and B2 == GPIO.HIGH and B3 == GPIO.HIGH:
            GPIO.output(LEDS[0], GPIO.HIGH)
        else:
            GPIO.output(LEDS[0], GPIO.LOW)

        # Logika dla L2
        if B2 == GPIO.HIGH:
            GPIO.output(LEDS[1], GPIO.HIGH)
        else:
            GPIO.output(LEDS[1], GPIO.LOW)

        # Logika dla L3
        if B3 == GPIO.HIGH:
            GPIO.output(LEDS[2], GPIO.HIGH)
        else:
            GPIO.output(LEDS[2], GPIO.LOW)

        # Logika dla L4
        if B3 == GPIO.LOW and B2 == GPIO.LOW and B1 == GPIO.HIGH:
            GPIO.output(LEDS[3], GPIO.HIGH)
            time.sleep(1)  # dodane, żeby dioda od razu nie gasła
        else:
            GPIO.output(LEDS[3], GPIO.LOW)

        # Krótkie opóźnienie, aby uniknąć błędów odczytu
        time.sleep(0.1)  # w sekundach

except KeyboardInterrupt:
    print("Przerwanie programu")

finally:
    GPIO.cleanup()
