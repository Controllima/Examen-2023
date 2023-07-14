class Persona:
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self._saldo = saldo
        self.nacionalidad = "peruana"

    def solicitar_datos(self):
        while True:
            try:
                self.nombre = input("Ingrese su nombre: ")
                self.edad = int(input("Ingrese su edad: "))
                self._saldo = float(input("Ingrese su saldo: "))
                break
            except ValueError:
                print("Error: El valor ingresado no es válido.")

    def cumpleanios(self):
        self.edad += 1

    def obtener_fecha_registro(self):
        fecha_actual = datetime.datetime.now()
        return fecha_actual.strftime("%Y-%m-%d %H:%M")

    def transferencia(self, monto, persona_destino):
        if self._saldo >= monto:
            self._saldo -= monto
            persona_destino._saldo += monto
            print("Transferencia realizada.")
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print("Saldo actual:", self._saldo)


# Crear instancias de la clase Persona
persona1 = Persona("", 0, 1000)
persona1.solicitar_datos()

persona2 = Persona("", 0, 500)
persona2.solicitar_datos()

# Realizar una transferencia de persona1 a persona2
monto_transferencia = 200
persona1.transferencia(monto_transferencia, persona2)

# Mostrar los saldos después de la transferencia
persona1.mostrar_saldo()
persona2.mostrar_saldo()
