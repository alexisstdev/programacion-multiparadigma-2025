# Sistema de Inventario

Sistema modular para gestionar productos e inventario.

## Proposito

Aplicacion simple para administrar productos, controlar stock y calcular valores de inventario.

## Estructura del Proyecto

```
proyecto-inventario/
├── main.py                 Programa principal
├── modulos/
│   ├── modelo.py          Clases Producto e Inventario
│   ├── operaciones.py     Funciones de negocio
│   └── utilidades.py      Funciones auxiliares
└── docs/
    └── manual_usuario.md  Documentacion de usuario
```

## Modulos

**modelo.py**: Define las clases Producto e Inventario con sus metodos
**operaciones.py**: Funciones para agregar, modificar, buscar y listar productos
**utilidades.py**: Funciones de validacion y formateo

## Ejecucion

```bash
python main.py
```

## Funcionalidades

- Agregar productos con codigo, nombre, precio y cantidad
- Modificar stock (agregar o reducir)
- Buscar productos por codigo
- Listar todos los productos en formato tabla
- Mostrar resumen con total de productos y valor del inventario