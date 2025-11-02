import json
import os
from modelos import Libro, Usuario, Biblioteca

ARCHIVO = "biblioteca.json"

def guardar_datos(biblioteca):
    data = {
        "libros": [libro.to_dict() for libro in biblioteca.libros],
        "usuarios": [{"nombre": u.nombre, "libros_prestados": [l.titulo for l in u.libros_prestados]} 
                     for u in biblioteca.usuarios]
    }
    with open(ARCHIVO, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def cargar_datos(biblioteca):
    if not os.path.exists(ARCHIVO):
        return
    
    try:
        with open(ARCHIVO, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for libro_data in data.get("libros", []):
            biblioteca.agregar_libro(Libro.from_dict(libro_data))
        
        for usuario_data in data.get("usuarios", []):
            usuario = Usuario(usuario_data["nombre"])
            for titulo in usuario_data.get("libros_prestados", []):
                libro = biblioteca.buscar_libro(titulo)
                if libro and libro.disponible:
                    usuario.prestar_libro(libro)
            biblioteca.agregar_usuario(usuario)
    except:
        pass