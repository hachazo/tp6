from __future__ import annotations
from abc import ABC, abstractmethod
import random
from typing import List


class Sujeto(ABC):

    @abstractmethod
    def agregar(self, observador: Observador) -> None:
        pass

    @abstractmethod
    def quitar(self, observador: Observador) -> None:
        pass

    @abstractmethod
    def notificar(self) -> None:
        pass

class Observador(ABC):

    @abstractmethod
    def actualizar(self, sujeto: Sujeto) -> None:
        pass