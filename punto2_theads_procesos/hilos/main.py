from hilo import *
from contador import *

hilos = []
contador = Contador()

for  i in range(4):
    hilo = Hilo(contador)
    hilos.append(hilo)
    hilo.start()
    
print("el valor final del contador es: ", contador.get_contador())