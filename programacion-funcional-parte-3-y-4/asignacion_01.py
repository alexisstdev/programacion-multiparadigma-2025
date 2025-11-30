def crear_transformador(funcion):
    def transformar(lista):
        return [funcion(x) for x in lista]
    return transformar


def crear_filtro(predicado):
    def filtrar(lista):
        return [x for x in lista if predicado(x)]
    return filtrar


def crear_reductor(funcion, valor_inicial):
    def reducir(lista):
        resultado = valor_inicial
        for x in lista:
            resultado = funcion(resultado, x)
        return resultado
    return reducir


def componer(*funciones):
    def ejecutar(dato):
        resultado = dato
        for funcion in funciones:
            resultado = funcion(resultado)
        return resultado
    return ejecutar


numeros = [1, -2, 3, -4, 5, -6, 7, 8, -9, 10]

pipeline = componer(
    crear_filtro(lambda x: x > 0),
    crear_transformador(lambda x: x ** 2),
    crear_reductor(lambda acc, x: acc + x, 0)
)

resultado = pipeline(numeros)
print(f"Resultado: {resultado}")