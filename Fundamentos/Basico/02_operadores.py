# Operadores

"""
Operadores aritméticos:
Se hacen cálculos como suma, resta, división y multiplicación.
"""

# Suma
suma = 5 + 3
print(suma)
print("Hello " + str(5))

# Resta
resta = 10 - 7
print(resta)

# Multiplicacion
multi = 6 * 4
print(multi)
print("Hello " * 5)

# Division
division = 10 / 3
print(division)

# Floor division
# Cuando se divide un entero, el resultado se redondea al entero más próximo
floor_division = 10 // 3
print(floor_division)

# Módulo (Devuelve el residuo de la división entera)
modulo = 9 % 2
print(modulo)

# Potencia (Exponente)
potencia = 2 ** 3 # Es igual a 8
print(potencia)


"""
Operadores de Comparacion
"""

# Mayor que
es_mayor = 10 > 5
print(es_mayor)

# Menor que
es_menor = 5 < 10
print(es_menor)

# Mayor o igual que
es_mayor_o_igual = 5 >= 5
print(es_mayor_o_igual)

# Menor o igual que
es_menor_o_igual = 5 <= 5
print(es_menor_o_igual)

# Igualdad
es_igual = 5 == 4
print(es_igual)

# Diferente
no_es_igual = 5 != 3
print(no_es_igual)

print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Bola") # Comparacion por Ordenacion Alfabetica por ASCII
print(len("Hola") >= len("Bola")) # Comparacion por Conteo de Caracteres
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")


"""
Operadores Logicos:
Logica Booleana (Tablas de la Verdad)
"""

# AND
es_par = (5 % 2 == 0) and (7 % 2 == 0)
print(es_par)

# OR
es_impar = (5 % 2 == 0) or (7 % 2 == 0)
print(es_impar)

# NOT
no_es_par = not es_par
print(no_es_par)
print(not (3 > 4))

# Operador de Negación Unaria
nulo = None
print(nulo)

# Damos prioridad a que se ejecute primero lo que esta dentro de parentesis
print(3 < 4 or ("Hola" > "Python" and 4 == 4))


"""
Operadores de asignación:
Asignar valores a una variable a lo largo del ciclo de vida de la variable.
"""
# =
x = 10
print(x) # x ahora contiene 10.

# +=
x += 5
print(x) # x incrementado en 5. Si contenía 10 antes, ahora tiene un valor de 15.

# -=
x -= 7
print(x) # x reducido en 7. Si contenía 15 antes, ahora tiene un valor de 8.

# /=
x /= 2
print(x) # x dividido por 2. Si contenía 8 antes, ahora tiene un valor de 4.

# *=
x *= 4 # x multiplicado por 4. Si contenía 4 antes, ahora tiene un valor de 16.
print(x)
