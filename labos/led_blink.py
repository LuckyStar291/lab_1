# Con este se configura los pines como IN u OUT, leer valores de sensores
import RPi.GPIO as GPIO
# Librería de python, maneja operaciones relacionadas con el tiempo, retardos (delays), medición de intervalos
import time

led_pin = 18  # Definimos valor del pin "led"

GPIO.setwarnings(False)  # Suprime-desactiva advertencias innecesarias en la consola de GPIO

GPIO.setmode(GPIO.BOARD)  # Configura la numeración de los GPIO, tiene 2 modos BCM y BOARD

GPIO.setup(led_pin, GPIO.OUT)  # Configurar el pin como salida
# En caso de ser entrada se lo puede configurar como:
#   - pull-up [GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)]
#   - pull-down [GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)]

# for -> usar cuando sabes cuántas veces se repetirá, se detiene cuando acaba la secuencia.
# while -> usar cuando no sabes cuántas veces se repetirá, se detiene cuando se cumple una condición para que se detenga.

# Parpadear infinitamente
try:  # Es recomendable el uso, cuando quieres finalizar un programa con ctrl+c, así no se detiene de manera abrupta y pasa a la línea except
    while True:
        # Genera un valor de salida HIGH-LOW
        GPIO.output(led_pin, GPIO.HIGH)  # Encender el LED
        time.sleep(1)                    # Retraso de 1 segundo
        GPIO.output(led_pin, GPIO.LOW)   # Apagar el LED
        time.sleep(1)                    # Retraso de 1 segundo
except KeyboardInterrupt:  # Captura la excepción cuando interrumpimos el programa, evitando la abrupta finalización
    GPIO.cleanup()  # Limpiar los pines GPIO al salir
