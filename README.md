# Contexto General

## 1. Introducción

- **Propósito del documento:**  
  Este documento define los requerimientos para el desarrollo de un sistema de gestión de ventas de una empresa de indumentaria femenina. El sistema permitirá a un analista de datos observar cómo las ventas varían en un periodo determinado.

- **Objetivo del proyecto:**  
  El objetivo del sistema es optimizar la administración de los productos disponibles y tener un registro de ventas de estos. Se busca, además, reducir el trabajo manual del personal de la empresa al automatizar la carga de productos y ventas realizadas.

## 2. Descripción general del sistema

- **Resumen del sistema:**  
  El sistema permitirá a la persona encargada de administrar la empresa gestionar los recursos de esta, como los diferentes tipos de prendas (tapados, pantalones, camisas y remeras). Además, podrá ver la disponibilidad de los productos, su valor y las ventas de los mismos.

- **Objetivos del sistema:**  
  1. Automatizar el proceso de inventario y ventas de los productos, permitiendo una gestión eficiente de los recursos.  
  2. Facilitar la consulta de los recursos de la empresa.  
  3. Reducir la dependencia del personal administrativo.  
  4. Asegurar la integridad y consistencia de los datos.

## 3. Programación Orientada a Objetos (OOP)

### Clases y Objetos
- Se definen distintas clases para representar entidades del sistema. Por ejemplo:
  - **Producto:** Clase base que contiene atributos comunes (código, nombre, precio y stock).
  - **Prenda:** Hereda de Producto y agrega atributos específicos (talla y color).
  - Clases derivadas de Prenda como **Pantalón**, **Camisa**, **Tapado** y **Remera**, que especializan la información agregando atributos (por ejemplo, tipo, manga o largo).

### Herencia
- Se utiliza para crear una jerarquía de clases. Las clases hijas reutilizan los atributos y métodos de la clase padre y, a la vez, pueden extender o sobreescribir la funcionalidad. Esto permite organizar el código y evitar redundancias.

### Polimorfismo
- Cada clase derivada implementa su propia versión del método `mostrar_informacion()`. Esto permite que, al invocar este método en objetos de distintas clases, se ejecute la función específica según el tipo de producto sin necesidad de conocer el tipo exacto del objeto.

### Encapsulamiento
- Los datos propios de cada objeto (atributos) se gestionan internamente dentro de sus clases. Esto protege la integridad de la información y establece interfaces claras a través de métodos como `mostrar_informacion()`.

### Uso de `super()`
- Se utiliza para llamar al constructor y métodos de la superclase, facilitando la reutilización del código y la extensión de funcionalidades en las clases derivadas.

## 4. Generación y Manipulación de Datos Aleatorios

### Uso de la librería `random`
- Se emplean funciones como `random.choice`, `random.randint` y `random.choices` para seleccionar elementos o generar números de forma aleatoria.
- **Ejemplo:** Seleccionar tallas y colores utilizando pesos que determinan la probabilidad de cada opción.

### Generación de fechas aleatorias
- La función `fecha_aleatoria()` utiliza el módulo `datetime` junto con `timedelta` para generar fechas aleatorias dentro de un intervalo definido. Esto permite simular ventas en distintas fechas.

## 5. Simulación de Ventas

### Instanciación de Objetos
- Se crean 1000 instancias de la clase `DetalleVenta`, cada una integrada por:
  - Un producto (instanciado en función del tipo: pantalón, camisa, tapado o remera)
  - Una cantidad aleatoria vendida
  - Una fecha aleatoria para la venta
  - Un identificador único de venta

### Detalle de Ventas
- La clase `DetalleVenta` extiende a `Venta` e incorpora atributos adicionales (`producto`, `cantidad` y `precio_unitario`) y métodos para calcular el total de la venta y mostrar la información detallada.

## 6. Visualización de Datos con Matplotlib

### Gráfico de Barras
- Se utiliza para representar las ventas agrupadas por tallas. Se construye un diccionario que acumula la cantidad vendida para cada talla y se grafica con barras.

### Gráfico de Torta (Pie Chart)
- Permite visualizar la distribución de ventas por color de las prendas. Se personaliza el gráfico resaltando ciertos sectores (por ejemplo, la porción correspondiente al color "Blanco") y se ajustan los colores de etiquetas y porcentajes.

### Gráfico de Línea
- Se usa para mostrar la evolución de las ventas a lo largo de distintos meses. Los datos se agrupan por mes y el gráfico permite identificar la tendencia de ventas en el período definido.
