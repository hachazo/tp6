import multiprocessing
from multiprocessing import freeze_support
import os
import time

if __name__ == '__main__':
    freeze_support()
    contador = multiprocessing.Manager().Value('i', 0) # Variable compartida (multiprocessing.Manager().Value se utiliza para crear una variable compartida)
    lista = []

    def cont_print():
        for _ in range(5000):
            with contador.get_lock():
                contador.value += 1
                print(contador.value)


    for _ in range(5):
        p = multiprocessing.Process(target=cont_print)
        lista.append(p)

    for pprocess in lista:
        pprocess.start()
            
    for pprocess in lista:
        pprocess.join()

# if __name__ == '__main__':
#     #info('Hilo main')
#     freeze_support()
#     mi_clase = Mi_clase()
#     process_start(mi_clase)

        