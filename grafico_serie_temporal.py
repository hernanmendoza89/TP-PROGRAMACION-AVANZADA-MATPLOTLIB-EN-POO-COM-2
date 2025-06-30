# grafico_serie_temporal.py
import matplotlib.pyplot as plt
from grafico_base import GraficoBase

# Este grafico va a mostrarnos una serie temporal de la tasa de natalidad nacional.
class GraficoSerieTemporal(GraficoBase):
    def plot(self):
        plt.figure(figsize=(10, 5))
        plt.plot(
            self.datos.index,
            self.datos["natalidad_argentina"],
            marker="o", color="#0072B2", lw=2
        )
        plt.title("Tasa de Natalidad en Argentina (2000–2023)")
        plt.xlabel("Año"); plt.ylabel("Tasa (%)")
        plt.grid(alpha=0.3)
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    from datos_natalidad import DatosNatalidad
    ruta = 'C:/Users/sherman/Desktop/tasa-natalidad-deis-2000-2023.csv'
    datos = DatosNatalidad(ruta).load()
    GraficoSerieTemporal(datos).plot()
