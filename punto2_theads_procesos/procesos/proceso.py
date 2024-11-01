from multiprocessing import Process
from multiprocessing import Lock

class Hilo(Process):
    
    def __init__(self,contador):
        super().__init__()
        self.__contador = contador
        self.__lock = Lock()
    
    def run(self):
        for i in range(5000):
            with self.__lock:
                self.__contador.incrementar()