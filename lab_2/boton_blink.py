import RPi.GPIO as GPIO #coontrola pines gpio
import time #permite uso de reloj

# Definiciones de pines
led_pin = 18
button_pin = 16

GPIO.setwarnings(False) # Suprimir advertencias

GPIO.setmode(GPIO.BOARD) #usar numeracion de pines GPIO

# Configuracion del pin del LED como salida y el botón como entrada (pull-up)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while True:
		if GPIO.input(button_pin) == GPIO.LOW:  # Si el botón está presionado
			GPIO.output(led_pin, GPIO.HIGH)     # Encender el LED
		else:
			GPIO.output(led_pin, GPIO.LOW)      # Apagar el LED
			time.sleep(0.1)  # Pequeño retraso para evitar rebotes
except KeyboardInterrupt:
	GPIO.cleanup()  # Limpiar los pines GPIO al salir
