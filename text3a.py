"""Crear un diccionario vacío"""
datos_persona = {}

"""Pedir por consola los valores para los keys"""
datos_persona['nombre'] = input("Ingrese el nombre: ")
datos_persona['apellidos'] = input("Ingrese los apellidos: ")
datos_persona['edad'] = input("Ingrese la edad: ")
datos_persona['dni'] = input("Ingrese el DNI: ")

"""Mostrar solo los values del diccionario"""
print("Valores del diccionario:")
for value in datos_persona.values():
    print(value)

"""Agregar un key adicional"""
datos_persona['profesion'] = input("Ingrese la profesión: ")

"""Eliminar el key 'dni'"""
del datos_persona['dni']

"""Mostrar el nuevo diccionario"""
print("Nuevo diccionario:")
print(datos_persona)
