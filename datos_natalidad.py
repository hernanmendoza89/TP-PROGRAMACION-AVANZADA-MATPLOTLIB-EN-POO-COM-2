# datos_natalidad.py
import pandas as pd

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
