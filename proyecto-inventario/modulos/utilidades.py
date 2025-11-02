"""
Módulo de utilidades.
Funciones auxiliares para validación y formateo.
"""


def validar_numero(texto, tipo=int):
    """
    Valida y convierte entrada de texto a número.
    
    Args:
        texto (str): Texto a convertir
        tipo: Tipo de dato (int o float)
        
    Returns:
        Número convertido o None si no es válido
    """
    try:
        return tipo(texto)
    except ValueError:
        return None


def validar_positivo(numero):
    """
    Verifica que un número sea positivo.
    
    Args:
        numero: Número a validar
        
    Returns:
        bool: True si es positivo, False en caso contrario
    """
    return numero is not None and numero > 0


def mostrar_tabla(productos):
    """
    Muestra productos en formato tabla.
    
    Args:
        productos (list): Lista de productos a mostrar
    """
    if not productos:
        print("No hay productos")
        return
    
    print("\n" + "=" * 70)
    print(f"{'CODIGO':<10} {'NOMBRE':<25} {'PRECIO':>10} {'STOCK':>10}")
    print("=" * 70)
    
    for p in productos:
        print(f"{p.codigo:<10} {p.nombre:<25} ${p.precio:>9.2f} {p.cantidad:>10}")
    
    print("=" * 70 + "\n")


def confirmar_accion(mensaje):
    """
    Solicita confirmación del usuario.
    
    Args:
        mensaje (str): Mensaje a mostrar
        
    Returns:
        bool: True si confirma, False en caso contrario
    """
    respuesta = input(f"{mensaje} (s/n): ").strip().lower()
    return respuesta == 's'