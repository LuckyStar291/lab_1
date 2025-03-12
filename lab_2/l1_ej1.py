import RPi.GPIO as GPIO
import time

# Pines
led1_pin = 18
led2_pin = 12
button_pin = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Configuración de pines como entrada y salida
GPIO.setup(led1_pin, GPIO.OUT)
GPIO.setup(led2_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variable auxiliar
c = 1
button_pressed = False
try:
    while True:
        # Leer el estado del botón
        button_state = GPIO.input(button_pin)
        
        # Si el botón está presionado y no se ha detectado antes
        if button_state == GPIO.LOW and not button_pressed:
            time.sleep(0.3)  # Antirrebote
            button_pressed = True
            c += 1
            if c > 4:
                c = 1

        # Si el botón no está presionado, resetear el estado
        if button_state == GPIO.HIGH:
            button_pressed = False


        if c == 1:  # Estado 1: Parpadeo alternado de los LEDs
            GPIO.output(led1_pin, GPIO.HIGH)
            GPIO.output(led2_pin, GPIO.LOW)
            time.sleep(1)
            GPIO.output(led1_pin, GPIO.LOW)
            GPIO.output(led2_pin, GPIO.HIGH)
            time.sleep(1)

        elif c == 2:  # Estado 2: Parpadeo simultáneo
            GPIO.output(led1_pin, GPIO.HIGH)
            GPIO.output(led2_pin, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(led1_pin, GPIO.LOW)
            GPIO.output(led2_pin, GPIO.LOW)
            time.sleep(2)

        elif c == 3:  # Estado 3: Ambos LEDs encendidos
            GPIO.output(led1_pin, GPIO.HIGH)
            GPIO.output(led2_pin, GPIO.HIGH)

        elif c == 4:  # Estado 4: Ambos LEDs apagados
            GPIO.output(led1_pin, GPIO.LOW)
            GPIO.output(led2_pin, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()  # Limpiar los pines GPIO al salir
