class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({self.anio}) [{estado}]"

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "anio": self.anio,
            "disponible": self.disponible
        }

    @staticmethod
    def from_dict(data):
        libro = Libro(data["titulo"], data["autor"], data["anio"])
        libro.disponible = data["disponible"]
        return libro


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            return True
        return False

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
            return True
        return False

    def __str__(self):
        return f"{self.nombre} - {len(self.libros_prestados)} libros prestados"

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "libros": [libro.titulo for libro in self.libros_prestados]
        }


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def buscar_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario.nombre.lower() == nombre.lower():
                return usuario
        return None

    def listar_disponibles(self):
        return [libro for libro in self.libros if libro.disponible]

    def listar_todos(self):
        return self.libros

    def __len__(self):
        return len(self.libros)