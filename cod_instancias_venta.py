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
    cantidad = random.randint(1, 5)
    precio_unitario = producto.precio
    id_venta = i
    detalle = DetalleVenta(id_venta, fecha, producto, cantidad, precio_unitario)
    ventas.append(detalle)