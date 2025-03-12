#Con este se configura los pines como IN u OUT, leer valores de sensores
import RPi.GPIO as GPIO
#libreria de python, maneja operaciones relacionadas con el tiempo, retardos(delays),medicion de intervalos
import time

led_pin = 18 #Definimos val del pin "led"

GPIO.setwarnings(False) #suprime-desactiva advertencias innecesarias en la consola de GPIO, permitiendo trabajar sin inconvenientes iniciales

GPIO.setmode(GPIO.BOARD) #configura la numeracion de los gpio, tiene 2 modos BCM ^ BOARD

GPIO.setup(led_pin, GPIO.OUT) # Configurar el # pin como salida
#En caso de ser entrada se lo puede configurar como:
#   - pull-up [GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)]
#   - pull-down [GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)]

#for -> usar cuando sabes cuántas veces se repetirá, se detiene cuando acaba la secuencia.
#while -> usar cuando no sabes cuántas veces se repetirá, se detiene cuando se cumple una condicion para que se detenga.
# Parpadear infinitamente
try: #es recomendable el uso, cuando quieres finalizar un programa ctl+c asi no se detendra de manera abrupta y pasa a ala linea except
	while True:
	    #genera un valor de salida HIGH-LOW
	    GPIO.output(led_pin, GPIO.HIGH)  # Encender el LED
	    time.sleep(1)                    # Retraso de 1 segundo
	    GPIO.output(led_pin, GPIO.LOW)   # Apagar el LED
	    time.sleep(1)                    # Retraso de 1 segundo
except KeyboardInterrupt: #captura la excepcion cuando interrumpimos el programa, evitando la abruota finalizacion
    GPIO.cleanup()  # Limpiar los pines GPIO al salir
