import multiprocessing

def incrementar(contador, lock):
    for _ in range(1):
        with lock:  # Asegura que solo un proceso modifique la variable a la vez
            contador.value += 1

if __name__ == "__main__":
    # Variable compartida
    contador = multiprocessing.Value('i', 0)  # 'i' indica un entero
    # Lock para sincronizar el acceso a la variable compartida
    lock = multiprocessing.Lock()

    # Crear una lista para los procesos
    procesos = []

    # Lanzar cuatro procesos
    for _ in range(4):
        proceso = multiprocessing.Process(target=incrementar, args=(contador, lock))
        procesos.append(proceso)
        proceso.start()

    # Esperar a que todos los procesos terminen
    for proceso in procesos:
        proceso.join()

    print(f"Valor final del contador: {contador.value}")