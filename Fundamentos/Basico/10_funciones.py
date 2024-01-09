# Funciones

"""
El uso de una función de Python es el primer paso para codificar 
después de las estructuras de datos y los condicionales básicos. 
Las funciones permiten la reutilización, lo que evita la duplicación de código. 
Cuando los proyectos reutilizan código con funciones, se vuelven más legibles y 
fáciles de mantener.
"""

# Las funciones son bloques de códigos que se pueden llamar desde
# diferentes partes del programa. Estas permiten organizar el 
# código y hacerlo más legible y reutilizable.

# Encapsular codigo que resolvera un problema en concreto.

# Si una función no devuelve explícitamente un valor, devuelve implícitamenteNone

def my_function():
    print("Esto es una funcion")

my_function()

def sum_two_values(param1,param2):
    sum = param1 + param2
    print(sum)

sum_two_values(5,3)

result1 = sum_two_values(3,1)

def sum_with_return(param1,param2):
    sum = param1 + param2
    return sum

result2 = sum_with_return(2,8)
print(sum_with_return(2,8))
print(result2)

def texto(name, lastname):
    print(f"{name} {lastname}")

texto(lastname="Ramirez", name="Yaneth")

# Parametros por defectos
# Parametros de palabra clave deben definirse en las propias funciones
def texto_default(name, lastname, alias="sin alias"):
    print(f"{name} {lastname} {alias}")

texto_default(lastname="Ramirez", name="Yaneth")

from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

print(arrival_time())

# Parametros dinamicos
# Paramentos de variable la función permite pasar cualquier 
# número de argumentos (incluido 0)

def print_texts(*texto):
    print(texto)

print_texts("Alonso","Yaneth","Ramona")

print_texts("Rambito")


def print_texts(*texto):
    for text in texto:
        print(text.upper())


print_texts("Alonso","Yaneth","Ramona")

print_texts("Rambito")

# Parametros de palabta clave variable
# Para que una función acepte cualquier número de argumentos de 
# palabra clave, debe usar una sintaxis similar. 
# En este caso, se requiere un asterisco doble

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")


