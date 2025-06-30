# grafico_barras_provincias.py
import matplotlib.pyplot as plt
from grafico_base import GraficoBase

# Esta clase nos representara un grafico de barras horizontal de provincias en 2023 con sus respectivos porcentajes.
class GraficoBarrasProvincias(GraficoBase):
    def plot(self):
        fila_2023 = self.datos.loc[self.datos["año"] == 2023].iloc[0]
        provincias = [
            c for c in self.datos.columns
            if c.startswith("natalidad_")
            and c != "natalidad_argentina"
        ]
        serie = fila_2023[provincias].sort_values(ascending=False)
        labels = [
            c.replace("natalidad_", "").replace("_", " ").title()
            for c in serie.index
        ]
        vals = serie.values

        fig, ax = plt.subplots(figsize=(8, 6))
        bars = ax.barh(labels, vals, color="skyblue")
        ax.invert_yaxis()
        maxv = vals.max()
        ax.set_xlim(0, maxv * 1.15)

        offset = maxv * 0.01
        for bar in bars:
            w = bar.get_width()
            y = bar.get_y() + bar.get_height()/2
            ax.text(w + offset, y, f"{w:.1f}", va="center", ha="left",
                    color="black", fontsize=10)
        ax.set_title("Natalidad por Provincia en 2023")
        ax.set_xlabel("Tasa (%)")
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    from datos_natalidad import DatosNatalidad
    ruta = 'C:/Users/sherman/Desktop/tasa-natalidad-deis-2000-2023.csv'
    datos = DatosNatalidad(ruta).load()
    GraficoBarrasProvincias(datos).plot()
