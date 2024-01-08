# Condicionales

# Los condicionales nos representan la manera de establecer
# flujos de ejecucion de nuestro codigo, es decir, decidir
# que parte del codigo se va a ejecutar dependiendo de una o varias condiciones
# Puedes anidar condicionales para hacer decisiones más complejas.

# Tipos de condicionales:
# 1. if (si) - solo ejecuta el bloque de instrucciones si
# la condicion es verdadera (True).

my_condition = True

if my_condition:
    print("Se ejecuta la condicion del if")

print("La ejecucion continua")

# 2. elif (más bien) - es como un else if, pero no tiene
# que estar justo después de un if ni antes de un else.
# Se puede poner en cualquier lugar entre los if y el else.

color = "negro"
if color == "azul":
    print("Es azul")
elif color == "rojo":
    print("Es rojo")
elif color == "verde":
    print("Es verde")
else:
    print("No es azul, ni rojo, ni verde")

# 3. else - si todas las condiciones anteriores son falsas,
# se ejecutará este bloque de instrucciones.

edad = 18
if edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")



