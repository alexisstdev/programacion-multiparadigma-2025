"""
Módulo de modelos de datos.
Contiene las clases principales para gestionar productos.
"""

class Producto:
    """
    Representa un producto en el inventario.
    
    Atributos:
        codigo: Identificador único del producto
        nombre: Nombre del producto
        precio: Precio unitario
        cantidad: Cantidad en stock
    """
    
    def __init__(self, codigo, nombre, precio, cantidad=0):
        """
        Inicializa un nuevo producto.
        
        Args:
            codigo (str): Código identificador
            nombre (str): Nombre del producto
            precio (float): Precio unitario
            cantidad (int): Cantidad inicial en stock
        """
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def agregar_stock(self, cantidad):
        """
        Agrega unidades al stock.
        
        Args:
            cantidad (int): Unidades a agregar
        """
        self.cantidad += cantidad
    
    def reducir_stock(self, cantidad):
        """
        Reduce unidades del stock.
        
        Args:
            cantidad (int): Unidades a reducir
            
        Returns:
            bool: True si fue exitoso, False si no hay suficiente stock
        """
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad
            return True
        return False
    
    def __str__(self):
        """Retorna representación en string del producto."""
        return f"{self.codigo} | {self.nombre} | ${self.precio:.2f} | Stock: {self.cantidad}"


class Inventario:
    """
    Gestiona el inventario de productos.
    
    Atributos:
        productos: Diccionario de productos indexados por código
    """
    
    def __init__(self):
        """Inicializa un inventario vacío."""
        self.productos = {}
    
    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario.
        
        Args:
            producto (Producto): Producto a agregar
        """
        self.productos[producto.codigo] = producto
    
    def buscar(self, codigo):
        """
        Busca un producto por código.
        
        Args:
            codigo (str): Código del producto
            
        Returns:
            Producto o None si no existe
        """
        return self.productos.get(codigo)
    
    def listar_todos(self):
        """
        Retorna lista de todos los productos.
        
        Returns:
            list: Lista de productos
        """
        return list(self.productos.values())
    
    def valor_total(self):
        """
        Calcula el valor total del inventario.
        
        Returns:
            float: Suma de precio * cantidad de todos los productos
        """
        return sum(p.precio * p.cantidad for p in self.productos.values())