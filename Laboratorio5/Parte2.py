# Script para pedir un número y determinar si es par o impar
numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

# Bucle para iterar sobre una lista de números e imprimir sus cuadrados
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(f"El cuadrado de {numero} es {numero ** 2}")

# Usar un bucle para solicitar entrada repetida hasta cumplir una condición
while True:
    entrada = input("Introduce un número mayor que 10: ")
    if int(entrada) > 10:
        print(f"¡Número {entrada} es mayor que 10!")
        break
    else:
        print("Número no válido. Intenta de nuevo.")