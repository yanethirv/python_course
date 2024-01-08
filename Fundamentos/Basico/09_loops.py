# Loops - Bucles - Ciclos

# Loops
# Es un mecanismo que nos sirve para iterar, es decir,
# realizar una acción repetida varias veces.

# Tipos de bucles:

# 1. While (Mientras)
# Es un bucle que se repite mientras la condición sea verdadera.
# La condición se evalúa al inicio del ciclo y si es cierta
# el bloque de código dentro del while se ejecuta.
# Si la condición cambia a falso, el bucle termina.
# Ejemplo: Mostrar los números del 0 al 9 usando while.
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 1
if my_condition == 10: # ES OPCIONAL
    print("Mi condicion es igual a 10")
else: # ES OPCIONAL
    print("Mi condicion es mayor a 10")

# 2. For (Para)
# Es un bucle que itera sobre un rango o listado de elementos.
# Se va a repetir el numero de veces de elementos que tengamos iterables.
# Cada vuelta del for esta accediendo a un elemento del listado.
# El for tiene tres partes separadas por puntos y comas :
# Inicialización de variable (Es obligatoria):
# Se utiliza para asignarle un valor inicial a la variable de control del bucle
# Condición (Opcional):
# Define cuándo debe seguir ejecutándose el bucle.
# Finalización (Opcional):
# Realiza alguna operación después de cada iteración.
# El bucle continúa hasta que la condición sea falsa.

numeros = range(5)
for numero in numeros:
    print("Soy el número", numero)

my_list = [35, 24, 62, 15]
for item in my_list:
    print("Soy el número", item)
else: # OPCIONAL
    print("Ya no hay más números en mi lista.")

# 3. Break y Continue
# Son sentencias especiales que permiten controlar el flujo del programa en los bucles
# Break:
# Detiene completamente el bucle y sale del mismo. No afecta al resto del script.
# Ejemplo: Buscar un número específico en una lista.
my_condition = 0

while my_condition < 10:
    my_condition += 1
    if my_condition == 7:
        print("Se detiene la ejecucion")
        break
    print(my_condition)

print("Sigue ejecutandose el codigo despues del break")
# Continue: NO ES ACONSEJABLE. MALA PRACTICA. OBSOLETO. Se puede manejar con un else u otra forma.
# Salta a la siguiente iteración del bucle. No afecta al resto del script.
# Ejemplo: Quitar números pares de una lista.
nums = [1, 2, 3, 4, 5, 6, 8, 9]
new_list = []
for num in nums:
    if num % 2 == 0:
        continue
    new_list.append(num)
    print(new_list)


# 3. Repeat (Repita)
# Es una versión simplificada de un bucle while que se repite una cantidad determinada
# de veces o hasta que se cumpla una condición.
repeat = "Hola"
times = 5
for i in range(times):
    print(repeat + " " + str(i))
