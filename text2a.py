import random

"""Crear lista con 10 valores aleatorios"""
lista_random = []
for _ in range(10):
    lista_random.append(random.randint(1, 100))

print("Lista aleatoria:", lista_random)

"""Llenar lista de cubos"""
lista_cubos = []
for num in lista_random:
    lista_cubos.append(num ** 3)

print("Lista de cubos:", lista_cubos)

"""Llenar lista de cuadrados"""
lista_cuadrados = []
for num in lista_random:
    lista_cuadrados.append(num ** 2)

print("Lista de cuadrados:", lista_cuadrados)

"""Mostrar la suma de las listas en orden inverso"""
suma_inversa = []
for i in range(len(lista_cubos)):
    suma_inversa.append(lista_cubos[i] + lista_cuadrados[-i - 1])

print("Suma inversa:", suma_inversa)
