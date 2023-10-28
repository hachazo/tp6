## El ejercicio pedía que se usaran procesos.
import threading
from multiprocessing import Process
import time
import random

class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo
    
    def getSaldo(self):
        return self._saldo
    
    def descontar(self, monto):
        self._saldo -= monto

class Tarjeta(threading.Thread):
    def __init__(self, id, cuenta):
        super().__init__()
        self._id = id
        self._cuenta = cuenta
    
    def run(self):
        for i in range(2):
            self._cuenta.descontar(100)
            time.sleep(1)
            print(f"Nuevo gasto - Tarjeta {self._id} - Nomto: 100")
    def getSaldo(self):
        return self._cuenta.getSaldo()

def main():
    cuenta = Cuenta(2000)
    tarjetas = []
    for i in range(10):
        tarjetas.append(Tarjeta(i, cuenta))
        tarjetas[i].start()
    
    for i in range(10):
        tarjetas[i].join()
    
    print(f"Saldo final: {cuenta.getSaldo()}")

if __name__ == '__main__':
    main()