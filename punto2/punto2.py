import threading
import time

contador = 0

def cont_print():
    for i in range(5000):
        global contador # Se usa para que el contador es una variable global y no local.
        contador += 1
        print(contador)

# crear theads
theads = []
for _ in range(5):
    thread = threading.Thread(target=cont_print)
    theads.append(thread)
    
# iniciar threads
for thread in theads:
    thread.start()

# esperar a que terminen los threads
for thread in theads:
     thread.join()
