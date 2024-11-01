from multiprocessing import Value

class Contador:
    
    def __init__(self):
        self.__contador = Value('i',0) # 'i' indica un entero
    
    def incrementar(self):
        self.__contador.value += 1
    
    def get_contador(self):
        return self.__contador.value