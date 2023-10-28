## El ejercicio pedía que se usaran procesos.
from multiprocessing import Process, Manager, Value
import time

class Cuenta:
    def __init__(self,saldo):
        self._saldo = Value('i', saldo)
    
    def getSaldo(self):
        return self._saldo.value
    
    def descontar(self, monto):
        self._saldo.value -= monto

class Tarjeta():
    def __init__(self, id, cuenta):
        super().__init__()
        self._id = id
        self._cuenta = cuenta
        
    def run(self):
        for i in range(2):
            self._cuenta.descontar(100)
            print(f"Nuevo gasto - Tarjeta {self._id} - Nomto: 100")
    
    def getSaldo(self):
        return self._cuenta.getSaldo()

def main():
    cuenta = Cuenta(2000)
    tarjetas = []
    for i in range(10):
        tarjetas.append(Process(target=Tarjeta(i, cuenta).run()))
        tarjetas[i].start()
        
    for i in range(10):
        tarjetas[i].join()
    
    print(f"Saldo final: {cuenta.getSaldo()}")

if __name__ == '__main__':
    main()