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