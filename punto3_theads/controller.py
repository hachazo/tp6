from model import *
import time

class controller():
    def __init__(self):
        self._conteo = Conteo()

    def iniciar(self):
        self._conteo.iniciar()

    def detener(self):
        self._conteo.detener()

    def parcial(self):
        self._conteo.parcial()
    
    def get_parciales(self):
        return self._conteo._parciales    

    # def attach(self, observer):
    #     self._conteo.attach(observer)
    
    # def detach(self, observer):
    #     self._conteo.detach(observer)
    
    # def notify(self):
    #     self._conteo.notify()
    
    # def get_parciales(self):
    #     return self._conteo._parciales
    
    # def get_contador(self):
    #     return self._conteo._contador
    
    # def get_subcontador(self):
    #     return self._conteo._subcontador
    
    # def get_estado(self):
    #     return self._conteo._estado
    