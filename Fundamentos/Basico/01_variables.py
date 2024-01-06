# Variables

'''
Buenas practicas:
- Las variables deben ser descriptivas y tener un nombre que indique su propósito.
- El nombre de una variable debe ir en minusculas y snake case
'''

my_string_variable = "My string variable" # Variable tipo String
print(my_string_variable)

my_int_variable = 5 # Variable tipo Int
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable) # Transformamos a String
print(my_int_to_str_variable)
print(type(my_int_to_str_variable)) # Imprimimos el tipo de dato

my_float_variable = 4.367
print(my_float_variable)

my_bool_variable = True # Variable tipo Boolean
print(my_bool_variable)

# Concatenacion de variables en un print. Le pasamos varios argumentos
print(my_string_variable, my_int_variable, my_float_variable, my_bool_variable)
print(my_string_variable, my_int_to_str_variable)
print("Valor de mi entero:", my_int_variable)

# Algunas Funciones Pre-Cargadas en el sistema
print(len(my_string_variable)) # Cuenta los caracteres incluidos los espacios

# Variables en una sola linea. !!!NO ES MUY BUENA PRACTICA!!!
name, lastname, alias, age = "Yaneth", "Ramirez", "Yanethirv", 43
print("Me llamo:", name, lastname, ". Mi edad es:", age, ", y mi Alias:", alias)

# Inputs
name = input("Ingrese su nombre:")
age = input("Ingrese su edad:")

print(name)
print(age)

# Python tiene un tipado debil
address: str = "Mi direccion"
address = 32
address = False
print(address) # No se puede asignarle un int a una var declarada como string