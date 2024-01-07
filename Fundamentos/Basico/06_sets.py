# Sets

# Set es un tipo de dato (clase set)
# ***Es una estructura como las listas pero no son modificables***
# No permiten valores duplicados, si se intenta agregar uno ya existente
# los elementos repetidos seran ignorados.

my_set = set()
print(type(my_set))

my_other_set = {"a","b",6}
print(type(my_other_set))

my_set = {"a","b",6}
my_other_set = {"Yaneth","Ramirez",43}
print(type(my_other_set))

print(len(my_other_set))


# Agregar elementos
# ***Un set no es una estructura ordenada (Es un map)***
# Utiliza un hash interno para agregar los elementos
my_other_set.add("Hola")
print(my_other_set)

# Un set no admite repetidos
# ***Si intentamos agregar otro valor repetido lo ignora***
my_other_set.add("Hola")
print(my_other_set)

# Buscar valores en un set
print("Hola" in my_other_set)
print("Holas" in my_other_set)

# Eliminar un elemento en un set
# Si el elemento existe en el conjunto lo elimina y devuelve True
# Si no existe lo elimina y devuelve False
# Si el elemento no esta en el conjunto lanza un error
my_other_set.remove("Hola")
print(my_other_set)

# Unir sets
union1 = my_set.union(my_other_set)
print(union1.union({"Alonso", 1.22}))

# Diferencias entre sets
intersection1 = union1.intersection(my_other_set)
difference1 = union1.difference(my_other_set)
symmetric_difference1 = union1.symmetric_difference(my_other_set)
print(f"Interseccion: {intersection1}")
print(f"Diferencia: {difference1}")
print(f"Simetrica diferencia: {symmetric_difference1}\n")

# Limpiar un set
# Para eliminar todos los elementos del set utilizamos el metodo clear()
my_other_set.clear()
print(my_other_set)

# Elimina la variable my_other_set
#del my_other_set
#print(my_other_set) #NameError: name 'my_other_set' is not defined
