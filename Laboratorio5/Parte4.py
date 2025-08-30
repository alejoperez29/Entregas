# Desarrollar un programa que simule una calculadora básica
def calculadora():
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    operacion = input("Elige una opción (1/2/3/4): ")
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if operacion == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operacion == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operacion == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operacion == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("¡No se puede dividir entre cero!")
    else:
        print("Operación no válida")

calculadora()

# Juego de adivinanza
import random
numero_aleatorio = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina el número entre 1 y 100: "))
    intentos += 1
    if intento < numero_aleatorio:
        print("¡Mayor!")
    elif intento > numero_aleatorio:
        print("¡Menor!")
    else:
        print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
        break