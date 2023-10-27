from multiprocessing import Process
from multiprocessing import freeze_support
import multiprocessing
import os
import time

class Miproceso(Process): 
    def __init__(self,contador):
        self.contador = contador
    def cont_print(self):
        for _ in range(50):
                self.contador += 1
                print(self.contador)
    

if __name__ == '__main__':
    contador = 0 # La variable contador no se comparte con los procesos, los procesos generan su propio contador al ejecutarse los procesos
    lista = [] # La lista es para poder generar 5 procesos y ejecutarlos al mismo tiempo
    p = Miproceso(contador)
    
    for _ in range(5): # Se generan 5 procesos
        p = Miproceso(contador)
        p = multiprocessing.Process(target=p.cont_print)
        lista.append(p)
        
    for pprocess in lista: # Se ejecutan los procesos   
        pprocess.start()
    
    # for pprocess in lista: # Se espera a que terminen los procesos
    #     pprocess.join() ## Puede no estar
    