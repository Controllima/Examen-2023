import datetime

class Persona:
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.salgo = saldo
        self.nacionalidad = "peruana"

    def solicitar_datos(self):
        while True:
            try:
                self.nombre = input("Ingrese su nombre: ")
                self.edad = int(input("Ingrese su edad: "))
                self.saldo = float(input("Ingrese su saldo: "))
                break
            except ValueError:
                print("Error: El valor ingresado no es válido.")

    def cumpleanios(self):
        self.edad += 1

    def obtener_fecha_registro(self):
        fecha_actual = datetime.datetime.now()
        return fecha_actual.strftime("%Y-%m-%d %H:%M")

# Crear instancia de la clase Persona
persona = Persona("", 0, 0)
persona.solicitar_datos()

# Incrementar la edad dos veces
persona.cumpleanios()
persona.cumpleanios()

# Mostrar la edad actualizada
print("Edad actualizada:", persona.edad)

# Obtener y mostrar la fecha de registro
fecha_registro = persona.obtener_fecha_registro()
print("Fecha de registro:", fecha_registro)
