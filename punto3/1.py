import multiprocessing

# Variable compartida (multiprocessing.Manager().Value se utiliza para crear una variable compartida)
if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")
    contador = 0

    # Función para incrementar el contador
    def incrementar_contador():
        for _ in range(5000):
            global contador
            contador  += 1

    # Crear cuatro procesos
    processes = []
    for _ in range(4):
        process = multiprocessing.Process(target=incrementar_contador)
        processes.append(process)

    # Iniciar los procesos
    for process in processes:
        process.start()

    # Esperar a que todos los procesos terminen
    for process in processes:
        process.join()

    # Imprimir el resultado
    print("Valor del contador:", contador)