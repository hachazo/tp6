import threading
import time
import threading

lock = threading.Lock()
contador = 0

def cont_print():
    for i in range(50):
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

# esperar a que terminen los threads para ejecutar el hola
for thread in theads:
     thread.join()
print("hola")