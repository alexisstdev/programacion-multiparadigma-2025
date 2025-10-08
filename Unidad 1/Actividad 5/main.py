from producto import Producto
from inventario import Inventario

def main():
    inv = Inventario()

    p1 = Producto("Laptop", 1200.0)
    p1.stock = 5
    p2 = Producto("Mouse", 25.5)
    p2.stock = 50
    p3 = Producto("Teclado", 45.0)
    p3.stock = 20
    p4 = Producto("Mouse", 30.0)
    p4.stock = 10

    inv.agregar_producto(p1)
    inv.agregar_producto(p2)
    inv.agregar_producto(p3)
    inv.agregar_producto(p4)

    print(inv)
    print(f"Total valor inventario: ${inv.total_valor_inventario():.2f}")

    buscado = inv.buscar_producto("Mouse")
    print(buscado)

    igual = Producto("Mouse", 30.0)
    print(igual == buscado)

    print(len(inv))

if __name__ == "__main__":
    main()