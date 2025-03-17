#EJERCICIO2 LABO4
import RPi.GPIO as GPIO
import time

# Configuración de pines
buzzer_pin = 2  # Pin GPIO para el buzzer naranja
button_pin = 3   # Pin GPIO para el botón amarillo

GPIO.setwarnings(False)  # Suprime-desactiva advertencias innecesarias en la consola de GPIO


# Configuración de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(button_pin) == GPIO.LOW:  # Botón presionado
            GPIO.output(buzzer_pin, GPIO.HIGH)  # Encender buzzer
        else:
            GPIO.output(buzzer_pin, GPIO.LOW)   # Apagar buzzer
        time.sleep(0.1)  # Pequeño retardo para evitar rebotes
except KeyboardInterrupt:
    GPIO.cleanup()  # Limpiar GPIO al salir