#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

# Definicje stanów dla diod LED
ON = True
OFF = False
L1 = False  # Stan diody LED1
L2 = False  # Stan diody LED2

def isOn(pin):
    # Funkcja sprawdza, czy pin wejściowy ma stan wysoki
    return GPIO.input(pin) == 1

def setPin(pin, state):
    # Funkcja ustawia stan wyjściowy na ON lub OFF dla wskazanego pinu
    GPIO.output(pin, state)

def pinSetup(pinsIn, pinsOut):
    # Konfiguracja pinów GPIO
    GPIO.setmode(GPIO.BOARD)  # Ustawienie trybu numeracji GPIO na BOARD
    GPIO.setwarnings(False)  # Wyłączenie ostrzeżeń

    # Konfiguracja pinów wejściowych
    for pin in pinsIn:
        GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)  # Pull-down dla wejścia

    # Konfiguracja pinów wyjściowych
    for pin in pinsOut:
        GPIO.setup(pin, GPIO.OUT)  # Ustawienie jako wyjście
        GPIO.output(pin, OFF)  # Poczatkowo wyłączenie diody

def main():
    # Definicje pinów GPIO
    pinsIn = [11]  # Lista pinów dla przycisków (wejściowe)
    pinsOut = [35, 37]  # Lista pinów dla diod LED (wyjściowe)

    # Konfiguracja pinów GPIO
    pinSetup(pinsIn, pinsOut)

    # Kopie list pinów do obsługi przycisków i diod
    LED = pinsOut.copy()  # Piny diod
    BTN = pinsIn.copy()  # Piny przycisków

    try:
        while True:
            # Sprawdzenie stanu przycisku
            if isOn(BTN[0]):
                print("BTN = ON")  # Informacja o stanie przycisku
                L1 = not L1  # Przełączenie stanu diody LED1
                L2 = not L1  # Stan diody LED2 jest przeciwny do LED1
                setPin(LED[0], L1)  # Ustawienie stanu diody LED1
                setPin(LED[1], L2)  # Ustawienie stanu diody LED2
                time.sleep(0.5)  # Opóźnienie dla stabilności
            else:
                print("BTN = OFF")  # Informacja o stanie przycisku
                L1 = 0  # Wyłączenie diody LED1
                L2 = 0  # Wyłączenie diody LED2
                setPin(LED[0], L1)  # Wyłączenie LED1
                setPin(LED[1], L2)  # Wyłączenie LED2

    except KeyboardInterrupt:
        # Obsługa przerwania programu (Ctrl+C)
        print("Czyszczenie pinów...")
        GPIO.cleanup()  # Czyszczenie konfiguracji GPIO

if __name__ == "__main__":
    main()  # Uruchomienie programu
