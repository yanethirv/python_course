# Diccionarios

my_dict = dict()
my_other_dict = {}
print(type(my_dict))  # <class 'dict'>
print(type(my_other_dict))  # <class 'dict'>

# Crear un diccionario con pares clave-valor
my_other_dict = {
    "nombre":"Yaneth",
    "apellido":"Ramirez",
    "edad":43,
    1:"Python"
}

my_dict = {
    "nombre":"Yaneth",
    "apellido":"Ramirez",
    "edad":43,
    1:1.66,
    "lenguajes":{"Python","PHP"},
    "hobbies":["Leer","Escribir"],
    "direccion":{
        "calle":"Av. Siempreviva",
        "numero":2075
        }
    
}

print(len(my_other_dict))
print(len(my_dict))

# Acceder a los valores de un dicionario por su clave
print("Nombre: ", my_other_dict["nombre"])
print("Edad: ", my_other_dict["edad"])

# Modificar el campo de un diccionario
my_other_dict["edad"]=48

# Agregar un nuevo campo clave-valor al diccionario
my_other_dict["nacionalidad"]="Venezolana"

# Comprobar si una clave se encuentra en el diccionario
print("Existe la llave nombre? ", "nombre" in my_dict)
print("Existe la llave 1? ", 1 in my_dict)
print("Existe la llave 2? ", 2 in my_dict)

# Comprobar si una valor se encuentra en el diccionario
print("Escribir" in my_dict["hobbies"])
print("Nadar" in my_dict["hobbies"])

# Usar el metodo items(), retorna un listado de cada uno de los items
print(my_dict.items())

# Usar el metodo keys(), retorna solo las claves del diccionario
print(my_dict.keys())

# Usar el metodo values(), retorna solo los valores del diccionario
print(my_dict.values())

# Usar el metodo fromkeys(), crea un nuevo diccionario nuevo sin valores
frutas = dict.fromkeys(["manzana","pera","platano"])

# Le pasamos un diccionario como parametro
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

# Le pasamos un diccionario como parametro para las claves,
# y el valor "Alonso" a todas las claves
my_new_dict = dict.fromkeys(my_dict, "Alonso")
print(my_new_dict)

# Creamos una lista a partir de un diccionario
# Toma solamente las claves como elementos para la lista
print(list(my_new_dict))

# Toma solamente los valores como elementos para la lista
print(list(my_new_dict.values()))
print()

# Crear un diccionario a partir de otro mediante el operador de asignación
otro_dicc = {**my_dict}
print(otro_dicc)

# Añadir o actualizar un elemento a un diccionario con el método append
my_dict["hobbies"].append("Correr")

#Eliminar un elemento del diccionario
my_dict.pop("nombre")
print(my_dict)

del my_dict["apellido"]
print(my_dict)

# Obtener el valor por defecto en caso de que no exista la clave
apellido = my_dict.get("apellido", "No existe apellido")
print(apellido)




