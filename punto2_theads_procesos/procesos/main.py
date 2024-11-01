from proceso import *
from contador import *

if __name__ == '__main__':

    hilos = []
    contador = Contador()

    for  i in range(4):
        h = Hilo(contador)
        h.start()
        h.join()


    print("El contador es {}".format(contador.get_contador()))