import funciones


def crear_fichero():
    archivo = open("notas.txt", "w")
    archivo.close()


def escribir_lista():
    tamaño = int(input("Ingrese el tamaño de la lista: "))
    lista = funciones.generar_lista_aleatoria(tamaño)

    archivo = open("notas.txt", "a")
    archivo.write("Lista generada: " + str(lista) + "\n")

    archivo.close()


def calcular_raiz():
    archivo = open("notas.txt", "a")
    archivo.write("Raíces cuadradas:\n")

    lista = funciones.leer_lista()

    for numero in lista:
        raiz = funciones.calcular_raiz_cuadrada(numero)
        archivo.write(str(raiz) + "\n")

    archivo.close()


# Crear el archivo "notas.txt"
crear_fichero()

# Escribir la lista en el archivo
escribir_lista()

# Calcular y escribir las raíces cuadradas en el archivo
calcular_raiz()