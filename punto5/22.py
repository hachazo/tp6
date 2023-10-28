from multiprocessing import Process, Value

class Cuenta:
    def __init__(self, saldo=0.0):
        self.saldo = Value('d', saldo)

    def descontar(self, cantidad):
        with self.saldo.get_lock():
            self.saldo.value -= cantidad

class Tarjeta(Process):
    def __init__(self, identificacion, cuenta):
        Process.__init__(self)
        self.identificacion = identificacion
        self.cuenta = cuenta

    def run(self):
        for _ in range(2):
            self.cuenta.descontar(100)

if __name__ == '__main__':
    # Crear una instancia de la clase Cuenta con un saldo inicial de $2000
    cuenta = Cuenta(2000)

    # Crear diez instancias de la clase Tarjeta asociadas a la cuenta creada
    tarjetas = [Tarjeta(identificacion=i, cuenta=cuenta) for i in range(10)]

    # Ejecutar el método start de cada instancia de Tarjeta (en paralelo)
    for tarjeta in tarjetas:
        tarjeta.start()

    # Esperar a que todos los procesos terminen
    for tarjeta in tarjetas:
        tarjeta.join()

    # Imprimir el saldo final de la cuenta
    with cuenta.saldo.get_lock():
        print(f"Saldo final de la cuenta: {cuenta.saldo.value}")