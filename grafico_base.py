# grafico_base.py
from abc import ABC, abstractmethod

# Hereda de la clase ABC para ser una clase abstracta.
# Esta clase se va a utilizar en todos los gráficos como herencia.
class GraficoBase(ABC):
    def __init__(self, datos):
        self.datos = datos

    @abstractmethod
    def plot(self):
        pass
