from producto import Producto

class Inventario:
    def __init__(self):
        self.__productos = {}

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Se requiere un objeto Producto")
        nombre = producto.nombre
        if nombre in self.__productos:
            existente = self.__productos[nombre]
            existente.stock = existente.stock + producto.stock
            existente.precio = producto.precio
        else:
            self.__productos[nombre] = producto

    def buscar_producto(self, nombre):
        return self.__productos.get(nombre)

    def total_valor_inventario(self):
        total = 0.0
        for p in self.__productos.values():
            total += p.precio * p.stock
        return total

    def __len__(self):
        return len(self.__productos)

    def __str__(self):
        lines = []
        for p in self.__productos.values():
            lines.append(str(p))
        return "\n".join(lines)