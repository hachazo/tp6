import time
import threading
from typing import List

class CronometroModel:
    def __init__(self):
        self._tiempo_actual = 0
        self._parciales = []
        self._observers = []

    def iniciar_cronometro(self):
        def contar():
            while True:
                time.sleep(1)
                self._tiempo_actual += 1
                self._notify_observers()

        t = threading.Thread(target=contar)
        t.daemon = True
        t.start()

    def detener_cronometro(self):
        self._tiempo_actual = 0
        self._parciales = []
        self._notify_observers()

    def crear_parcial(self):
        self._parciales.append(self._tiempo_actual)
        self._notify_observers()

    def get_tiempo_actual(self):
        return self._tiempo_actual

    def get_parciales(self):
        return self._parciales

    def add_observer(self, observer):
        self._observers.append(observer)

    def _notify_observers(self):
        for observer in self._observers:
            observer.update()

# Observador (Observer): El observador es notificado cuando cambia el estado del modelo.
class CronometroObserver:
    def __init__(self, model):
        self._model = model

    def update(self):
        pass