import time


def medir_tiempo_ejecucion(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")
        return resultado
    return wrapper


@medir_tiempo_ejecucion
def multiplicacion(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado


# Ejemplos de llamadas a la función multiplicacion decorada
resultado1 = multiplicacion(2, 3, 4)
print("Resultado 1:", resultado1)

resultado2 = multiplicacion(5, 6, 7, 8)
print("Resultado 2:", resultado2)

resultado3 = multiplicacion(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Resultado 3:", resultado3)
