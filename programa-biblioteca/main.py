from modelos import Biblioteca
from operaciones import agregar_libro, agregar_usuario, mostrar_libros, mostrar_disponibles, prestar_libro, devolver_libro
from datos import guardar_datos, cargar_datos

def mostrar_menu():
    print("\n=== SISTEMA DE GESTION DE BIBLIOTECA ===")
    print("1. Agregar libro")
    print("2. Agregar usuario")
    print("3. Mostrar todos los libros")
    print("4. Mostrar libros disponibles")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Salir")
    return input("Opcion: ").strip()

def main():
    biblioteca = Biblioteca()
    cargar_datos(biblioteca)
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            agregar_libro(biblioteca)
            guardar_datos(biblioteca)
        elif opcion == "2":
            agregar_usuario(biblioteca)
            guardar_datos(biblioteca)
        elif opcion == "3":
            mostrar_libros(biblioteca)
        elif opcion == "4":
            mostrar_disponibles(biblioteca)
        elif opcion == "5":
            prestar_libro(biblioteca)
            guardar_datos(biblioteca)
        elif opcion == "6":
            devolver_libro(biblioteca)
            guardar_datos(biblioteca)
        elif opcion == "7":
            print("Saliendo")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()