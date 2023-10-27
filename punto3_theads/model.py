import threading
import time
from observer_aplicado import *

class Observer(Sujeto):
    def __init__(self):
       super().__init__() 
       self._observers: List [Observador] = []
    
    def agregar(self, observador):
        self._observers.append(observador)

    def quitar(self, observador):
        self._observers.remove(observador)

    def notificar(self):
        for observer in self._observers:
            observer.actualizar(self)
            
class Conteo(Observer):
    def __init__(self):
        super().__init__()
        self._contador = 0
        self._subcontador = 0
        self._estado = False
        self._parciales = []

    def iniciar(self):
        self._estado = True
        self._contador = 0
        self._subcontador = 0
        self._parciales = []
        self._thread = threading.Thread(target=self._contar)
        self._thread.start()

    def detener(self):
        self._estado = False
        self._thread.join()

    def parcial(self):
        self._parciales.append(self._subcontador)
        self._subcontador = 0

    def _contar(self):
        while self._estado:
            self._contador += 1
            self._subcontador += 1
            time.sleep(1)
            print(self._contador)
            print("contando")
            self.notificar()
    