import RPi.GPIO as GPIO
import time

heater_pin = 12  # Pin del calentador
fan_pin = 18  # Pin del ventilador

# Configuración de GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(heater_pin, GPIO.OUT)  # Calentador
GPIO.setup(fan_pin, GPIO.OUT)  # Ventilador

# Función para controlar el sistema de temperatura
def control_temperatura(temp):
    if temp < 12:
        GPIO.output(heater_pin, GPIO.HIGH)
        GPIO.output(fan_pin, GPIO.LOW)  
        print("Alerta! temperatura baja....")
        time.sleep(1)
        print("..... Encendiendo calentador .....")
        time.sleep(1)
        print("Tiempo estimado de optimizacion 10 seg\n ")
        time.sleep(10)
        GPIO.output(heater_pin, GPIO.LOW)
        print("Temperatura óptima, temperatura actual 12 C\n")

    elif temp > 20:
        GPIO.output(heater_pin, GPIO.LOW) 
        GPIO.output(fan_pin, GPIO.HIGH)  
        print("Alerta! temperatura alta....")
        time.sleep(1)
        print("..... Encendiendo ventilador .....")
        time.sleep(1)
        print("Tiempo estimado de optimizacion 10 seg\n ")
        time.sleep(10)
        GPIO.output(fan_pin, GPIO.LOW)
        print("Temperatura óptima, temperatura actual 20 C\n")

    else:
        GPIO.output(heater_pin, GPIO.LOW)  # Apagar ambos
        GPIO.output(fan_pin, GPIO.LOW)
        print("Temperatura óptima\n")


try:
    while True:
        try:
            temp = float(input("La temperatura actual es: "))
            control_temperatura(temp)  # Controlar el sistema
        except ValueError:
            print("¡Error! Debes ingresar un número válido.")
 

except KeyboardInterrupt:
    GPIO.cleanup()  # Limpiar los pines
