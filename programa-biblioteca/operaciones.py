from modelos import Libro, Usuario

def agregar_libro(biblioteca):
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    anio = input("Año: ")
    try:
        anio = int(anio)
    except:
        anio = 2000
    libro = Libro(titulo, autor, anio)
    biblioteca.agregar_libro(libro)
    print("Libro agregado")

def agregar_usuario(biblioteca):
    nombre = input("Nombre: ")
    usuario = Usuario(nombre)
    biblioteca.agregar_usuario(usuario)
    print("Usuario agregado")

def mostrar_libros(biblioteca):
    libros = biblioteca.listar_todos()
    if not libros:
        print("No hay libros")
        return
    print("\nLibros:")
    for i, libro in enumerate(libros, 1):
        print(f"{i}. {libro}")
    print()

def mostrar_disponibles(biblioteca):
    libros = biblioteca.listar_disponibles()
    if not libros:
        print("No hay libros disponibles")
        return
    print("\nLibros disponibles:")
    for i, libro in enumerate(libros, 1):
        print(f"{i}. {libro}")
    print()

def prestar_libro(biblioteca):
    nombre = input("Nombre usuario: ")
    usuario = biblioteca.buscar_usuario(nombre)
    if not usuario:
        print("Usuario no encontrado")
        return
    
    titulo = input("Titulo libro: ")
    libro = biblioteca.buscar_libro(titulo)
    if not libro:
        print("Libro no encontrado")
        return
    
    if usuario.prestar_libro(libro):
        print("Libro prestado")
    else:
        print("Libro no disponible")

def devolver_libro(biblioteca):
    nombre = input("Nombre usuario: ")
    usuario = biblioteca.buscar_usuario(nombre)
    if not usuario:
        print("Usuario no encontrado")
        return
    
    titulo = input("Titulo libro: ")
    libro = biblioteca.buscar_libro(titulo)
    if not libro:
        print("Libro no encontrado")
        return
    
    if usuario.devolver_libro(libro):
        print("Libro devuelto")
    else:
        print("Este usuario no tiene ese libro")