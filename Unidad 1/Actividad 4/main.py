from libro import Libro

def main():
    print("=== SISTEMA DE GESTIÓN DE BIBLIOTECA ===")
    print(f"Bienvenido a la {Libro.biblioteca}\n")
    
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605)
    libro3 = Libro("1984", "George Orwell", 1949)
    
    print("=== ESTADO INICIAL DE LOS LIBROS ===")
    libro1.mostrar_estado()
    libro2.mostrar_estado()
    libro3.mostrar_estado()
    
    print("\n=== REALIZANDO PRÉSTAMOS ===")
    
    libro1.prestar()
    libro3.prestar()
    
    print("\nIntentando prestar el mismo libro nuevamente:")
    libro1.prestar()
    
    print("\n=== ESTADO DESPUÉS DE PRÉSTAMOS ===")
    libro1.mostrar_estado()
    libro2.mostrar_estado()
    libro3.mostrar_estado()
    
    print("\n=== REALIZANDO DEVOLUCIONES ===")
    
    libro1.devolver()
    
    print("\nIntentando devolver un libro no prestado:")
    libro2.devolver()
    
    print("\n=== ESTADO FINAL DE LOS LIBROS ===")
    libro1.mostrar_estado()
    libro2.mostrar_estado()
    libro3.mostrar_estado()
    
    print(f"\nTodos los libros pertenecen a: {Libro.biblioteca}")
    print("Esto es un atributo de clase compartido por todas las instancias.")

if __name__ == "__main__":
    main()