import RPi.GPIO as GPIO
import time

# Pin definitions
led_pins = [13, 15, 12, 18]
button1_pin = 16 #SUBE
button2_pin = 19 #BAJA

# Configuración de GPIO
GPIO.setmode(GPIO.BOARD)
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

c = 0

# Función para actualizar los LEDs
def update_leds():
    for i in range(4):
        GPIO.output(led_pins[i], (c >> i) & 1)

#imprime los valores
def print_values():
    print(f"Decimal: {c}, Binario: {bin(c)}, Hexadecimal: {hex(c)}")

# Bucle principal
try:
    while True:
        # Aumentar contador con botón 1
        if GPIO.input(button1_pin) == GPIO.LOW:
            c = (c + 1) % 16  # Límite de 0 a 15
            update_leds()
            print_values()  # Imprimir valores
            time.sleep(0.5)  # Evitar rebotes

        # Disminuir contador con botón 2
        if GPIO.input(button2_pin) == GPIO.LOW:
            if c>0:
                c-=1

#            c = (c - 1) % 16  # Límite de 0 a 15
            update_leds()
            print_values()
            time.sleep(0.5)  # Evitar rebotes
except KeyboardInterrupt:
    GPIO.cleanup()  # Limpiar los pines al salir


