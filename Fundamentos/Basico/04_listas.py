# Listas

# Una lista es una coleccion o conjunto de elementos
# Una lista es mutable
my_list = list()
my_other_list = []

print(len(my_list))

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(planets, len(planets))

my_other_list = [43, 1.66, "Yaneth", True]
print(type(my_other_list))

# Operaciones con listas

# Acceder a los elementos por indice (comenzando desde cero)
print("Elemento en la posicion cero: ", planets[0])
print(planets[-1])
print(planets[-4])
print(planets.count('Mars'))

age, height, name, lastname = my_other_list
print(age)

# Concatenar listas
print(planets + my_other_list)

# Agregar elementos a la lista
planets.append("Pluto")
print(planets)

# Insertar un elemento en una posición específica
planets.insert(2, 'Ceres')
print(planets)

# Remover un elemento que se conoce dentro de la lista (el primero que consigue)
planets.remove('Ceres')
print(planets)

# Remover el ultimo elemento de la lista
# Pop (desapilar)
planets.pop()
print(planets)

# Remover un elemento de la lista en una posicion especifica
# Debemos asignarlo a una variable
pop_planets = planets.pop(1)
print(pop_planets)

# Elimina el elemento por indice (pero no lo retorna como pop)
del planets[2]

# Cambiar el valor de un elemento de una lista
planets[5] = "Jupiter"

# Copiar una lista. 
copied_planets = planets[:]
copied_planets = list(planets)
my_new_planets = planets.copy()

# Mostrar si un elemento esta en una lista
print("Mars" in planets)

# Limpiar una lista (quitar todos los elementos)
planets.clear()
print(planets)
print(my_new_planets)

# Revertir los valores de una lista
my_new_planets.reverse()
print(my_new_planets)

# Ordenar una lista
my_new_planets.sort()
print(my_new_planets)
my_new_planets.sort(reverse=True)
print(my_new_planets)

# Crear sublistas o extraer parte de una lista
first_three_planets = copied_planets[:3]
print(first_three_planets)

print(copied_planets)

# No incluye el ultimo, solo va hasta antes del ultimo
middle_two_planets = copied_planets[1:3] 
print(middle_two_planets)

# Devuelve el segundo a último
second_last_planet = copied_planets[-2]
print(second_last_planet)

# Devuelve la última posición y todo lo que hay después
last_planet = copied_planets[-1]
print(last_planet)

# Contar cuantos planetas hay en nuestra lista
num_of_planets = len(copied_planets)
print(f"There are {num_of_planets} planets.")

# Slice con pasos diferentes, es decir, saltarse algunos elementos
primeros_cinco_planetas = copied_planets[::2]
print(primeros_cinco_planetas)