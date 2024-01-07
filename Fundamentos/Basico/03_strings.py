# Strings

my_string = "Mi string"
my_other_string = 'Mi otro string'
print(len(my_string))
print(len(my_other_string))

# Concatenar strings
print(my_string + " " + my_other_string)
# Usando comas para concatenar sin espacio en blanco
print(my_string, my_other_string)

# Salto de linea
my_new_line_string = "String con \n salto de linea"
print(my_new_line_string)

# Tabulacion
my_tabbed_string = "\tEste es un string con tabulacion"
print(my_tabbed_string)

# Acceder a los caracteres de un string
first_character = my_string[0]  # Obtener el primer carácter
print(first_character)

# Formateo
name, lastname, age = "Yaneth", "Ramirez", 43

print("Mi nombre es {} {} y mi edad es {}".format(name, lastname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, lastname, age))

#Interpolacion de Datos, la mejor opcion
formatted_string = f"Mi nombre es {name} {lastname} y mi edad es {age}"
print(formatted_string)

# Desempaquetado de caracteres
lenguaje = "Python"
a, b, c, d, e, f = lenguaje
print(a)
print(e)

# Division
lenguaje_slice = lenguaje[1:3]
print(lenguaje_slice)

lenguaje_slice = lenguaje[1:]
print(lenguaje_slice)

lenguaje_slice = lenguaje[-2]
print(lenguaje_slice)

# Evitar caracteres
lenguaje_slice = lenguaje[0:6:2]
print(lenguaje_slice)

# Reverse
reversed_language = lenguaje[::-1]
print(reversed_language)

# Funciones del sistema para strings
print(lenguaje.capitalize())
print(lenguaje.upper())
print(lenguaje.count("t"))
print(lenguaje.isnumeric())
print(lenguaje.lower().isupper())
print(lenguaje.startswith('Py'))
