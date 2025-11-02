# Sistema de Gestion de Biblioteca

Sistema modular para administrar libros y usuarios en una biblioteca.

## Estructura

```
Proyecto Final/
├── main.py          Programa principal
├── modelos.py       Clases Libro, Usuario, Biblioteca
├── operaciones.py   Funciones de gestion
├── datos.py         Persistencia JSON
└── README.md        Documentacion
```

## Clases

**Libro**: titulo, autor, anio, disponible
**Usuario**: nombre, libros_prestados
**Biblioteca**: administra libros y usuarios

## Funcionalidades

- Agregar libros y usuarios
- Listar libros disponibles y todos
- Prestar y devolver libros
- Persistencia automatica en JSON

## Ejecucion

```bash
python main.py
```

Los datos se guardan en biblioteca.json