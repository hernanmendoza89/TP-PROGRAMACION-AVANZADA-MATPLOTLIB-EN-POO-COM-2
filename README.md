# Sistema de Visualización de Natalidad en Argentina

Este proyecto automatiza la carga, el procesamiento y la generación de tres tipos de gráficos que permiten analizar la evolución de la tasa de natalidad nacional y provincial en Argentina entre 2000 y 2023.

## Características Principales

### Carga y Preparación de Datos
- Lectura de un CSV con registros mensuales de natalidad.  
- Conversión de la columna `indice_tiempo` a índice de tipo fecha.  
- Cálculo automático de la columna auxiliar `año`.  

### Diseño Modular y POO
- **DatosNatalidad**: clase encargada de leer y formatear el DataFrame.  
- **GraficoBase**: clase abstracta que define la interfaz `plot()`.  
- **Subclases de gráfico** (`GraficoSerieTemporal`, `GraficoBarrasProvincias`, `GraficoPastelTop3`):  
  Heredan de `GraficoBase` y cada una implementa `plot()` para un tipo de visualización distinto.  
- Aplicación de herencia, polimorfismo y encapsulamiento para mantener el código limpio y extensible.  

## Visualizaciones con Matplotlib

### Serie Temporal  
Evolución de la tasa nacional de natalidad (2000–2023) con línea y marcadores.

### Barras Horizontales  
Ranking de provincias para el año 2023, mostrando tasas y etiquetas de valor.

### Gráfico de Pastel  
Proporción de las tres provincias con mayor natalidad promedio a lo largo del período analizado.

## Tecnologías Utilizadas
- **Lenguaje:** Python 3.7+  
- **Bibliotecas:**  
  - `pandas` (manipulación y preparación de datos)  
  - `matplotlib` (generación de gráficos)  
