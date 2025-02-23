def sumar_numeros():
    n = int(input("¿Cuántos números quieres sumar?: "))
    suma = sum(int(input(f"Ingresa el número {i+1}: ")) for i in range(n))
    print(f"La suma total es: {suma}")

def invertir_numero():
    num = input("Ingresa un número para invertirlo: ")
    print(f"Número invertido: {num[::-1]}")

def datos_usuario():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    profesion = input("Profesión: ")
    print(f"Hola {nombre}, tienes {edad} años y trabajas como {profesion}.")

def valores_unicos():
    lista = list(map(int, input("Ingresa números separados por espacios: ").split()))
    print(f"Valores únicos: {list(set(lista))}")

# Prueba cada función llamándola aquí
sumar_numeros()
invertir_numero()
datos_usuario()
valores_unicos()
