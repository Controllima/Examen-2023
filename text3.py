def ingresar_datos():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("Error: Ingrese números válidos.")

def division(num1, num2):
    while True:
        try:
            resultado = num1 / num2
            return resultado
        except ZeroDivisionError:
            print("Error: División entre cero.")
            num2 = float(input("Ingrese un segundo número distinto de cero: "))

def evaluar_suma(num1, num2):
    while True:
        try:
            suma = num1 + num2
            if suma < 10:
                raise ValueError("Error: La suma es menor que 10.")
            return suma
        except ValueError as e:
            print(e)
            num1, num2 = ingresar_datos()

# Ingresar datos
num1, num2 = ingresar_datos()

# Realizar la división
resultado_division = division(num1, num2)
print("Resultado de la división:", resultado_division)

# Evaluar la suma
suma = evaluar_suma(num1, num2)
print("Suma:", suma)
