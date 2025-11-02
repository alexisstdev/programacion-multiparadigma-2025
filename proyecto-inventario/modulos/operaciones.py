"""
Módulo de operaciones de negocio.
Funciones para gestionar las operaciones del inventario.
"""

from modulos.modelo import Producto
from modulos.utilidades import validar_numero, validar_positivo, mostrar_tabla


def agregar_producto(inventario):
    """
    Agrega un nuevo producto al inventario.
    
    Args:
        inventario (Inventario): Inventario donde agregar
    """
    print("\n--- Agregar Producto ---")
    codigo = input("Codigo: ").strip()
    
    if inventario.buscar(codigo):
        print("Error: Codigo ya existe")
        return
    
    nombre = input("Nombre: ").strip()
    precio = validar_numero(input("Precio: "), float)
    cantidad = validar_numero(input("Cantidad: "), int)
    
    if not validar_positivo(precio) or cantidad is None or cantidad < 0:
        print("Error: Datos invalidos")
        return
    
    producto = Producto(codigo, nombre, precio, cantidad)
    inventario.agregar_producto(producto)
    print("Producto agregado")


def modificar_stock(inventario):
    """
    Modifica el stock de un producto.
    
    Args:
        inventario (Inventario): Inventario a modificar
    """
    print("\n--- Modificar Stock ---")
    codigo = input("Codigo del producto: ").strip()
    producto = inventario.buscar(codigo)
    
    if not producto:
        print("Producto no encontrado")
        return
    
    print(f"Stock actual: {producto.cantidad}")
    print("1. Agregar stock")
    print("2. Reducir stock")
    opcion = input("Opcion: ").strip()
    
    cantidad = validar_numero(input("Cantidad: "), int)
    
    if not validar_positivo(cantidad):
        print("Cantidad invalida")
        return
    
    if opcion == "1":
        producto.agregar_stock(cantidad)
        print("Stock actualizado")
    elif opcion == "2":
        if producto.reducir_stock(cantidad):
            print("Stock actualizado")
        else:
            print("Stock insuficiente")


def buscar_producto(inventario):
    """
    Busca y muestra un producto.
    
    Args:
        inventario (Inventario): Inventario donde buscar
    """
    print("\n--- Buscar Producto ---")
    codigo = input("Codigo: ").strip()
    producto = inventario.buscar(codigo)
    
    if producto:
        print(f"\n{producto}")
    else:
        print("Producto no encontrado")


def listar_productos(inventario):
    """
    Lista todos los productos.
    
    Args:
        inventario (Inventario): Inventario a listar
    """
    productos = inventario.listar_todos()
    mostrar_tabla(productos)


def mostrar_resumen(inventario):
    """
    Muestra resumen del inventario.
    
    Args:
        inventario (Inventario): Inventario a resumir
    """
    print("\n--- Resumen ---")
    print(f"Total productos: {len(inventario.productos)}")
    print(f"Valor total: ${inventario.valor_total():.2f}\n")