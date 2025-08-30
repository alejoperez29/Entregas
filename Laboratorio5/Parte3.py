# Crear una lista de estudiantes y mostrar cada uno
estudiantes = ["Ana", "Luis", "Pedro", "Maria"]
for estudiante in estudiantes:
    print(estudiante)

# Crear un diccionario de información de contacto
contactos = {
    "Juan": "juan@mail.com",
    "Pedro": "pedro@mail.com",
    "Maria": "maria@mail.com"
}
for nombre, correo in contactos.items():
    print(f"{nombre}: {correo}")

# Permitir al usuario agregar elementos a una lista o diccionario
nuevo_estudiante = input("Introduce el nombre de un nuevo estudiante: ")
estudiantes.append(nuevo_estudiante)
print(f"Lista actualizada de estudiantes: {estudiantes}")