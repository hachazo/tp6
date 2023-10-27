from controller import controller
from model import *
from observer_aplicado import *
from observer_aplicado import *
import time

class Cronometro(controller,Observador):
    def __init__(self):
        super().__init__()
        #Observer.agregar(self)
    
    def mostrar_cronometro(self):
        print(f"Tiempo actual: {self._conteo._contador} segundos")
        
        print("Parciales:")
        for i, parcial in enumerate(self._conteo._parciales):
            print(f"Parcial {i + 1}: {parcial} segundos")
            
    def actualizar(self):
        self._mostrar_cronometro()
        
class Main(controller):
    modelo = Conteo()
    #Observer.agregar(modelo)
    view = Cronometro()
    
    while True:
        print("\nOpciones:")
        print("1. Iniciar cronómetro")
        print("2. Detener cronómetro")
        print("3. Crear parcial")
        print("4. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            modelo.iniciar()
        elif opcion == "2":
            modelo.detener()
        elif opcion == "3":
            modelo.parcial()
        elif opcion == "4":
            modelo.detener()
            break
        else:
            print("Opción inválida")
            
if __name__ == "__main__":
    Main()