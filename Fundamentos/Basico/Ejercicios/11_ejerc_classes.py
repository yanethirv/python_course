class Juguete:
    nombre = "",
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre,
        self.precio = precio

    def __str__(self):
        return (f"Juguete: {self.nombre}, precio: {self.precio}")

j1 = Juguete("Dinosaurio", 10.5)

print(str(j1))