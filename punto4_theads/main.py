from __future__ import annotations
import threading
import time
import random

class Corredor(threading.Thread):
    def __init__(self, numero):
        super().__init__()
        self._numero = numero
        self._tiempo = random.randint(5, 10)

    def run(self):
        print(f"Inicia Corredor {self._numero}")
        time.sleep(self._tiempo)
        print(f"Tiempo: {self._tiempo} segundos")

def main():
    corredor1 = Corredor(1)
    corredor2 = Corredor(2)
    corredor3 = Corredor(3)
    corredor4 = Corredor(4)

    corredor1.start()
    corredor1.join()
    corredor2.start()
    corredor2.join()
    corredor3.start()
    corredor3.join()
    corredor4.start()
    corredor4.join()

    print(f"Tiempo total {corredor1.tiempo + corredor2.tiempo + corredor3.tiempo + corredor4.tiempo} segundos")

if __name__ == '__main__':
    main()
    