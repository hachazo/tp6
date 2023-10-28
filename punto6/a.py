# El error se produce al querer adquirir el lock dos veces en el mismo proceso, ya que el lock solo se puede adquirir una vez por proceso.
# para solucionar el problema primero se tiene que liverar el lock y luego volver a adquirirlo.
# Se supone que yo adquiero el lock y lo livero pero antes de liverarlo trabajo con el recurso compartido.
from multiprocessing import Process
from multiprocessing import Lock

def task(lock):
    print('Adquiriendo el Lock...', flush=True)
    with lock:
            # Mientras tenga el lock 
            # <--- Trabajo con el recurso compartido
            # lock.release() # <--- libero el lock
        
        # print('Adquirido el Lock otra vez ...', flush=True)
        # with lock: # Como ya no tengo el lock lo puedo volver a adquirir
        #     pass <-- Trabajo con el recurso compartido
              # lock.release() # <--- libero el lock
        
if __name__ == '__main__':
    lock = Lock()
    process = Process(target=task, args=(lock,))
    process.start()
    process.join()
    
