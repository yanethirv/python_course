# Tuplas

# Una tupla es un conjunto de valores, los cuales no pueden modificarse
# Una tupla es inmutable, no se pueden agregar nuevos valores

# Crea una tupla vacia
my_tuple = tuple()
mi_tupla = ()

my_tuple = (43, 1.66, "Yaneth", "Ramirez", True)
mi_tupla = ("a", "b")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count(43))

# Nos indica el indice del primer elemento que encuentra con valor 43
print(my_tuple.index(43))

# Operaciones con tuplas
sum_tuple = my_tuple + mi_tupla
print(sum_tuple)

multi_tuple = sum_tuple * 3
print(multi_tuple)

print(multi_tuple[:])
print(multi_tuple[::-1])
print(multi_tuple[1:3])
print(multi_tuple[::-1])
print(multi_tuple[1:-1])
print(multi_tuple[::2])
print(multi_tuple[::-2])

# Elimina una tupla
del multi_tuple
#print(multi_tuple) #NameError: name 'multi_tuple' is not defined
