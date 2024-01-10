# Clases en Python

"""
Una clase es un molde o plantilla para crear objetos, estos
objetos son instancias de la clase y tienen atributos y métodos 
propios de esa clase. 
Las clases permiten agrupar todas las variables y funciones
que se relacionan entre si, formando un grupo lógico de objetos.
"""
# Una clase es un objeto definido a nuestra medida

# Una clase puede hacer cosas mediante un constructor que sea
# capaz de recibir parametros o argumentos

## Creación de una clase
class Person:
    """Clase que representa a una persona."""
    ## Atributo de la clase (común a todos los objetos)
    nombre = "Desconocido"
    apellido = "Desconocido"
    # Constructor de Clase
    # Crea por primera vez el objeto (Es mutable)
    def __init__(self, name, lastname, alias = "Sin alias"):
        """Inicializa con los parámetros recibidos."""
        # Propiedad Publica
        self.fullname = f"{name} {lastname} ({alias})"
        # Propiedad Privada
        self.__nombre = name # Privado

    # Creamos una lectura (Getter encubierto en una funcion)
    def get_nombre(self):
        return self.__nombre

    # Debemos pasar el parametro self por defecto
    def saludar(self):
        """Muestra un mensaje de saludo personalizado."""
        print(f"Hola, soy {self.fullname}")
    

my_person = Person("Alonso","Portillo")
print(f"{my_person.nombre} {my_person.apellido}")
print(my_person.fullname)
my_person.saludar()


my_other_person = Person("Yaneth","Ramirez","Yanethirv")
print(f"{my_other_person.nombre} {my_other_person.apellido}")
print(my_other_person.fullname)
my_other_person.saludar()
my_other_person.fullname = "Hector de leon (el loco de los perros)"
print(my_other_person.fullname)
my_other_person.__nombre = 'Change'
print(my_other_person.__nombre)
print(my_other_person.get_nombre())

class Juguete:
    nombre = "",
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre,
        self.precio = precio

    # Sobrecarga del metodo str
    # Se utiliza para salidas informales. PARA CODIGO DE PRODUCCION
    #se pueden generar representacionesde texto, de forma que 
    # cuando se haga print o se asigne se haga una representacion legible para humanos.
    def __str__(self):
        return (f"Juguete: {self.nombre}, precio: {self.precio}")

    # Sobrecarga del metodo repr
    # Se utiliza para salidas tecnicas. PARA CODIGO DE DESARROLLO
    # Lo utilizamos cuando queremos generar salidas de depuracion
    def __repr__(self):
        return (f"Juguete: {self.nombre}, precio: {self.precio}")

j1 = Juguete("Dinosaurio", 10.5)

print(str(j1))
print(repr(j1))