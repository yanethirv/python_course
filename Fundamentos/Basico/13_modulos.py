# MODULOS

# Es esa libreria o lugar donde tenemos codigo
# Los ficheros se comportan como modulos

# Forma General
import modulos

modulos.my_function()
modulos.sum_two_values(3, 8)

# Forma Especifica
from modulos import my_function, sum_two_values

my_function()
sum_two_values(2,2)

# Modulos del sistema
import math

print(math.pi)
print(math.pow(2,8))

# Importar Pi del Modulo math y colocarle el alias pi_value
from math import pi as pi_value

print(f"Pi Value {pi_value}")