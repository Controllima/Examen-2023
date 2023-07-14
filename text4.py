import random


def almacenar_numeros_aleatorios():
    numeros = []
    for _ in range(10):
        numero = random.randint(1, 100)
        numeros.append(numero)
    print("Lista de números aleatorios:")
    print(numeros)
    return numeros


def almacenar_numeros_no_repetidos(numeros):
    numeros_no_repetidos = list(set(numeros))
    print("Lista de números no repetidos:")
    print(numeros_no_repetidos)
    return numeros_no_repetidos


def ordenar_numeros(numeros):
    numeros_ordenados_mayor_a_menor = sorted(numeros, reverse=True)
    numeros_ordenados_menor_a_mayor = sorted(numeros)
    print("Lista ordenada de mayor a menor:")
    print(numeros_ordenados_mayor_a_menor)
    print("Lista ordenada de menor a mayor:")
    print(numeros_ordenados_menor_a_mayor)
    return numeros_ordenados_mayor_a_menor, numeros_ordenados_menor_a_mayor


def obtener_mayor_numero(numeros):
    mayor_numero = max(numeros)
    print("El mayor número de la lista es:", mayor_numero)
    return mayor_numero


# Llamadas a las funciones
numeros_aleatorios = almacenar_numeros_aleatorios()
numeros_no_repetidos = almacenar_numeros_no_repetidos(numeros_aleatorios)
numeros_ordenados_mayor, numeros_ordenados_menor = ordenar_numeros(numeros_no_repetidos)
mayor_numero = obtener_mayor_numero(numeros_no_repetidos)
