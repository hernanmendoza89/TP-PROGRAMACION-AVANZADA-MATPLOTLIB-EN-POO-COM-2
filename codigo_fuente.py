import pandas as pd
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

# Creamos las clases "DatosNatalidad" y "GraficoBase".
# Carga y prepara los datos de natalidad.
class DatosNatalidad:
    def __init__(self, ruta_csv):
        self.ruta_csv = ruta_csv
        self.datos = None

    def load(self):
        df = pd.read_csv(
            self.ruta_csv,
            parse_dates=["indice_tiempo"],
            dayfirst=True
        )
        df.set_index("indice_tiempo", inplace=True)
        df["año"] = df.index.year
        self.datos = df
        return self.datos

    def columnas_provincia(self):
        return [
            c for c in self.datos.columns
            if c.startswith("natalidad_") and c != "natalidad_argentina"
        ]

# Hereda de la clase ABC para ser una clase abstracta.
# Esta clase se va a utilizar en todos los gráficos como herencia.
class GraficoBase(ABC):
    def __init__(self, datos):
        self.datos = datos

    @abstractmethod
    def plot(self):
        pass

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


if __name__ == "__main__":
    # cargo datos
    datos_natalidad = DatosNatalidad('C:/Users/sherman/Desktop/tasa-natalidad-deis-2000-2023.csv')
    df = datos_natalidad.load()

    # Creo cada gráfico y lo muestro
    GraficoSerieTemporal(df).plot()
    GraficoBarrasProvincias(df).plot()
    GraficoPastelTop3(df).plot()
