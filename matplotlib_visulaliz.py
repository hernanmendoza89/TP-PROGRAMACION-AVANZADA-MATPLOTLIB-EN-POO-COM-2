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