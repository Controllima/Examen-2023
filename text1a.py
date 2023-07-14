
"""Suma de las edades de los trabajadores"""
suma_edades = edad1 + edad2
print("La suma de las edades de los trabajadores es: {}".format(suma_edades))

"""Mostrar los trabajadores y sus edades"""
print("Trabajadores:")
for i, trabajador in enumerate(trabajadores):
    print("Trabajador", i + 1, "-", "Nombre:", trabajador[0], "Edad:", trabajador[1])
