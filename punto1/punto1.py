import threading
import time

def holamundo(id):
    print("Hola mundo desde el hilo", id)
    time.sleep(id)
    return

if __name__ == "__main__":
    for i in range(6):
        t = threading.Thread(target=holamundo, args=(i,))
        t.start()
        t.join()
