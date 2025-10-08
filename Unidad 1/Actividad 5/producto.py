class Producto:
    def __init__(self, nombre, precio):
        if precio <= 0:
            raise ValueError("Precio debe ser mayor que 0")
        self.nombre = nombre
        self._precio = float(precio)
        self.__stock = 0

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("Stock no puede ser negativo")
        self.__stock = int(value)

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        if value <= 0:
            raise ValueError("Precio debe ser mayor que 0")
        self._precio = float(value)

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: ${self._precio:.2f}, Stock: {self.__stock}"

    def __eq__(self, other):
        if not isinstance(other, Producto):
            return False
        return self.nombre == other.nombre