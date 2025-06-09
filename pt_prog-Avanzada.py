import random  
from datetime import datetime, timedelta  
import matplotlib.pyplot as plt 

# DEFINICIÓN DE CLASES.

# Creo la clase base producto y las subclases heredadas(prenda,pantalón,camisa y tapado).
class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

#Retorna una cadena con la info de producto.
    def mostrar_informacion(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}"

class Prenda(Producto):
    def __init__(self, codigo, nombre, precio, stock, talla, color):
        # Llama al constructor de Producto para inicializar los atributos comunes
        super().__init__(codigo, nombre, precio, stock)
        # Inicializa los atributos específicos de una prenda
        self.talla = talla
        self.color = color

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        info += f", Talla: {self.talla}, Color: {self.color}"
        return info

class Pantalón(Prenda):
    def __init__(self, codigo, nombre, precio, stock, talla, color, tipo):
        super().__init__(codigo, nombre, precio, stock, talla, color)
        self.tipo = tipo  

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        info += f", Tipo de pantalón: {self.tipo}"
        return info

class Camisa(Prenda):
    def __init__(self, codigo, nombre, precio, stock, talla, color, manga):
        super().__init__(codigo, nombre, precio, stock, talla, color)
        self.manga = manga

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        info += f", Manga: {self.manga}"
        return info

class Tapado(Prenda):
    def __init__(self, codigo, nombre, precio, stock, talla, color, largo):
        super().__init__(codigo, nombre, precio, stock, talla, color)
        self.largo = largo

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        info += f", Largo: {self.largo}"
        return info

class Remera(Prenda):
    def __init__(self, codigo, nombre, precio, stock, talla, color, manga):
        super().__init__(codigo, nombre, precio, stock, talla, color)
        self.manga = manga

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        info += f", Manga: {self.manga}"
        return info

# Clase Venta: representa una venta simple con id y fecha
class Venta:
    def __init__(self, id_venta, fecha):
        # Inicializa identificador y fecha de la venta
        self.id_venta = id_venta
        self.fecha = fecha

    def __repr__(self):
        # Define cómo se mostrará la venta
        return f"Venta(id={self.id_venta}, fecha='{self.fecha}', "

# Clase DetalleVenta, hereda de venta
class DetalleVenta(Venta):
    def __init__(self, id_venta, fecha, producto, cantidad, precio_unitario):
        # Inicializa los atributos heredados de Venta
        super().__init__(id_venta, fecha)
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        
    def calcular_total(self):
        # Retorna el total multiplicando la cantidad por el precio unitario
        return self.cantidad * self.precio_unitario
    
    def mostrar_informacion(self):
        # Combina la información básica de Venta con los detalles de la venta y el total
        info = super().__repr__()
        info += (
          f"producto={self.producto.nombre}, cantidad={self.cantidad}, "
          f"precio_unitario=${self.precio_unitario}, total=${self.calcular_total()})"
        )
        return info


# DATOS PREDEFINIDOS Y PARÁMETROS

# Listas de nombres permitidos para cada tipo de prenda
nombres_permitidos_pantalon = ["jean clasico", "sastrero", "escocia", "black"]
nombres_permitidos_camisa   = ["pink", "grey"]
nombres_permitidos_tapado   = ["florencia", "ginger", "perla"]
nombres_permitidos_remera   = ["rebeca", "yoana", "isabel", "paris"]

# Listas de talles y colores disponibles
talles  = ["S", "M", "L", "XL", "XXL"]
colores = ["Blanco", "Negro", "Bordo", "Azul", "Beige"]

# Pesos,permitiendo que algunas opciones se seleccionen con mayor probabilidad
pesos_talles = [15, 22, 35, 20, 8]         
pesos_colores = [20, 30, 17, 23, 10]         

# Genera una fecha aleatoria en formato "dd/mm/yyyy" entre dos fechas
def fecha_aleatoria(inicio, fin):
    diferencia = fin - inicio
    dias_aleatorios = random.randint(0, diferencia.days)
    fecha_generada = inicio + timedelta(days=dias_aleatorios)
    return fecha_generada.strftime("%d/%m/%Y")

# Intervalo de fechas para las ventas: desde 05/03/2025 hasta 05/06/2025
fecha_inicio = datetime(2025, 3, 5)
fecha_fin    = datetime(2025, 9, 5)


# GENERACIÓN DE 1000 INSTANCIAS VENTAS(DetalleVenta)

ventas = []  # Lista donde se almacenarán las ventas

# Ciclo para generar 1000 ventas
for i in range(1, 1001):
    # Selecciona aleatoriamente el tipo de producto
    tipo_producto = random.choice(["pantalon", "camisa", "tapado", "remera"])
    
    # Selecciona atributos comunes utilizando pesos para talles y colores
    talle = random.choices(talles, weights=pesos_talles, k=1)[0]
    color = random.choices(colores, weights=pesos_colores, k=1)[0]
    precio = random.randint(15000, 50000)  # Precio aleatorio entre 15000 y 50000
    stock = 100  # Stock fijo para todos los productos
    # Crea un código único
    codigo = f"{tipo_producto[:3].upper()}{i:03d}"

    # Según el tipo de producto, se asignan atributos y se instancia el objeto correspondiente
    if tipo_producto == "pantalon":
        nombre = random.choice(nombres_permitidos_pantalon)
        tipo = nombre  
        producto = Pantalón(codigo, nombre, precio, stock, talle, color, tipo)
        
    elif tipo_producto == "camisa":
        nombre = random.choice(nombres_permitidos_camisa)
        manga = random.choice(["corta", "larga"])
        producto = Camisa(codigo, nombre, precio, stock, talle, color, manga)
        
    elif tipo_producto == "tapado":
        nombre = random.choice(nombres_permitidos_tapado)
        largo = random.choice(["corto", "largo"])
        producto = Tapado(codigo, nombre, precio, stock, talle, color, largo)
        
    elif tipo_producto == "remera":
        nombre = random.choice(nombres_permitidos_remera)
        manga = random.choice(["corta", "larga"])
        producto = Remera(codigo, nombre, precio, stock, talle, color, manga)
    
    # Genera una fecha aleatoria para la venta dentro del intervalo definido
    fecha = fecha_aleatoria(fecha_inicio, fecha_fin)
    # Selecciona una cantidad aleatoria vendida (entre 1 y 5)
    cantidad = random.randint(1, 5)
    # El precio unitario se toma del precio del producto
    precio_unitario = producto.precio
    # Usa el índice de la iteración para asignar un id único a cada venta
    id_venta = i
    # Crea una instancia de DetalleVenta con todos los datos
    detalle = DetalleVenta(id_venta, fecha, producto, cantidad, precio_unitario)
    # Agrega la venta a la lista
    ventas.append(detalle)

# GRÁFICO DE BARRAS, VENTAS POR TALLA

# Inicializa un diccionario para contar ventas de cada talla
ventas_por_talla = {talla: 0 for talla in talles}

# Recorrer cada venta y acumular la cantidad vendida según la talla del producto
for venta in ventas:
    ventas_por_talla[venta.producto.talla] += venta.cantidad

print("Ventas por talla:", ventas_por_talla)

# Preparación de datos para el gráfico 
tallas_x = list(ventas_por_talla.keys())
ventas_y = list(ventas_por_talla.values())

# Configuración y generación del gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(tallas_x, ventas_y, color="steelblue")
plt.xlabel("Talla")
plt.ylabel("Cantidad Vendida")
plt.title("Ventas por Talla")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()


# GRÁFICO DE TORTA: VENTAS POR COLOR

# Inicializa el diccionario para contar ventas por color
ventas_por_color = {color: 0 for color in colores}

# Acumula las ventas según el color del producto
for venta in ventas:
    ventas_por_color[venta.producto.color] += venta.cantidad

print("Ventas por color:", ventas_por_color)

# Preparar etiquetas y valores para el gráfico de torta
etiquetas_color = list(ventas_por_color.keys())
valores_ventas_color = list(ventas_por_color.values())

# Asigna colores reales para cada etiqueta en el gráfico
mapeo_colores = {
    "Blanco": "white",
    "Negro": "black",
    "Bordo": "darkred",
    "Azul": "blue",
    "Beige": "beige"
}
colores_torta = [mapeo_colores[color] for color in etiquetas_color]

# Generación del gráfico de torta
plt.figure(figsize=(8, 6))
rebanadas, textos, etiquetas_autom = plt.pie(valores_ventas_color,
                                             labels=etiquetas_color,
                                             colors=colores_torta,
                                             autopct='%1.1f%%',
                                             startangle=90)

# Resaltar con contorno la porción "Blanco" 
for rebanada, etiqueta in zip(rebanadas, etiquetas_color):
    if etiqueta == "Blanco":
        rebanada.set_edgecolor("black")
        rebanada.set_linewidth(1.5)

# Ajustar el color del texto en la porción "Negro" 
for etiqueta, texto_auto in zip(etiquetas_color, etiquetas_autom):
    if etiqueta == "Negro":
        texto_auto.set_color("white")

plt.title("Ventas por Color")
plt.show()


# GRÁFICO DE LINEA: VENTA POR MES(Marzo, Abril, Mayo, Junio, Julio, Agosto, Septiembre)

# Inicializa un diccionario para acumular ventas de los meses 3, 4 y 5
ventas_por_mes = {3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 200}

# Recorre cada venta, convirtiendo la fecha de string a objeto datetime
for venta in ventas:
    fecha_dt = datetime.strptime(venta.fecha, "%d/%m/%Y")
    mes = fecha_dt.month
    if mes in ventas_por_mes:
        ventas_por_mes[mes] += venta.cantidad

# Ordena los meses y prepara los datos para el gráfico
meses_ordenados = sorted(ventas_por_mes.keys())  
nombres_mes = {3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 
               7: "Julio", 8: "Agosto", 9: "Septiembre"}
etiquetas_mes = [nombres_mes[mes] for mes in meses_ordenados]
valores_ventas_mes = [ventas_por_mes[mes] for mes in meses_ordenados]

# Generación del gráfico de línea
plt.figure(figsize=(8, 6))
plt.plot(etiquetas_mes, valores_ventas_mes, marker="o", linestyle="--", color="purple", linewidth=2)
plt.xlabel("Mes")
plt.ylabel("Cantidad Vendida")
plt.title("Ventas por Mes (Marzo-Abril-Mayo-Junio-Julio-Agosto-Septiembre)")
plt.grid(True)
plt.show()
    
