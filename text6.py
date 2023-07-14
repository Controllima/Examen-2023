import random
import math


def generar_lista_aleatoria(tamaño):
    lista = []
    for _ in range(tamaño):
        numero = random.randint(1, 100)
        lista.append(numero)
    return lista


def calcular_raiz_cuadrada(numero):
    return math.sqrt(numero)


def leer_lista():
    archivo = open("notas.txt", "r")
    contenido = archivo.readlines()
    archivo.close()

    # Obtener la lista generada previamente
    for linea in contenido:
        if linea.startswith("Lista generada"):
            lista_texto = linea.split(": ")[1]
            lista = eval(lista_texto)
            return lista
