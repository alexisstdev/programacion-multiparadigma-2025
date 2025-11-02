"""
Programa principal del sistema de inventario.
Controla el flujo y menú principal.
"""

from modulos.modelo import Inventario
from modulos.operaciones import (
    agregar_producto,
    modificar_stock,
    buscar_producto,
    listar_productos,
    mostrar_resumen
)


def mostrar_menu():
    """
    Muestra el menú principal.
    
    Returns:
        str: Opción seleccionada por el usuario
    """
    print("\n=== SISTEMA DE INVENTARIO ===")
    print("1. Agregar producto")
    print("2. Modificar stock")
    print("3. Buscar producto")
    print("4. Listar productos")
    print("5. Mostrar resumen")
    print("6. Salir")
    return input("Seleccione opcion: ").strip()


def main():
    """
    Función principal que ejecuta el programa.
    Inicializa el inventario y controla el flujo del menú.
    """
    inventario = Inventario()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            modificar_stock(inventario)
        elif opcion == "3":
            buscar_producto(inventario)
        elif opcion == "4":
            listar_productos(inventario)
        elif opcion == "5":
            mostrar_resumen(inventario)
        elif opcion == "6":
            print("Saliendo del sistema")
            break
        else:
            print("Opcion invalida")


if __name__ == "__main__":
    main()