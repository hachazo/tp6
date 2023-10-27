from model import CronometroObserver, CronometroModel
class CronometroView(CronometroObserver):
    def __init__(self, model):
        super().__init__(model)
        self._model.add_observer(self)
    
    def update(self):
        self.mostrar_cronometro()

    def mostrar_cronometro(self):
        tiempo_actual = self._model.get_tiempo_actual()
        parciales = self._model.get_parciales()
        print(f"Tiempo actual: {tiempo_actual} segundos")
        print("Parciales:")
        for i, parcial in enumerate(parciales):
            print(f"Parcial {i + 1}: {parcial} segundos")

def main():
    model = CronometroModel()
    view = CronometroView(model)

    while True:
        print("\nOpciones:")
        print("1. Iniciar cronómetro")
        print("2. Detener cronómetro")
        print("3. Crear parcial")
        print("4. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            model.iniciar_cronometro()
        elif opcion == "2":
            model.detener_cronometro()
        elif opcion == "3":
            model.crear_parcial()
        elif opcion == "4":
            break

if __name__ == "__main__":
    main()
