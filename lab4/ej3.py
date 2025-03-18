import RPi.GPIO as GPIO
import time

# Definir pines
LED1 = 2
LED2 = 3

# Configuración de pines
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

# Frecuencia inicial
freq = 1  

def seq1(freq):
    """ Alterna los LEDs con la frecuencia definida """
    GPIO.output(LED1, GPIO.HIGH)
    GPIO.output(LED2, GPIO.LOW)
    time.sleep(1 / freq)
    
    GPIO.output(LED1, GPIO.LOW)
    GPIO.output(LED2, GPIO.HIGH)
    time.sleep(1 / freq)

while True:
    try:
        with open("Controller_emb.txt", "r") as file:
            line = file.readline().strip()
            if "Freq(Hz)=" in line:
                f = line.split("=")[-1].strip()  # Extraer el número después del '='
                freq = float(f)  # Convertir a float
    except Exception as e:
        print(f"Error leyendo el archivo: {e}")

    seq1(freq)
