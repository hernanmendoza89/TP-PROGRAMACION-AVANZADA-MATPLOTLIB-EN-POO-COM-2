# grafico_pastel_top3_y_main.py
import matplotlib.pyplot as plt
from datos_natalidad import DatosNatalidad
from grafico_base import GraficoBase  
from abc import ABC

# Esta clase nos mostrara un gráfico de pastel de las 3 provincias con mayor natalidad promedio.
class GraficoPastelTop3(GraficoBase):
    def plot(self):
        provincias = [
            c for c in self.datos.columns
            if c.startswith("natalidad_")
            and c != "natalidad_argentina"
        ]
        promedios = self.datos[provincias].mean()
        top3 = promedios.sort_values(ascending=False).head(3)

        labels = [
            c.replace("natalidad_", "").replace("_", " ").title()
            for c in top3.index
        ]
        sizes = top3.values
        colors = ['#79ADDC', '#FFEE93', '#84DCC6']

        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(
            sizes, labels=labels, autopct="%1.1f%%",
            startangle=140, colors=colors,
            textprops={'fontsize': 10, 'color': '#333'}
        )
        ax.set_title("Top 3 Provincias por Natalidad Promedio (2000–2023)")
        ax.axis("equal")
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    ruta = 'C:/Users/sherman/Desktop/tasa-natalidad-deis-2000-2023.csv'
    # Cargo y muestro el gráfico
    datos = DatosNatalidad(ruta).load()
    GraficoPastelTop3(datos).plot()
