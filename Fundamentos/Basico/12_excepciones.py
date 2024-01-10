# Manejo de Excepciones (Errores)

try:
    num = int(input("Ingrese un número entero: "))
    divisor = 10
    resultado = num / divisor
    print("No ha ocurrido un error.")
# Se ejecuta si se produce una excepcion
except:
    print("Ha ocurrido un error.")
# Se ejecuta si no se produce una excepcion
else: ### OPCIONAL
    print("La ejecucion continua correctamente")
# Se ejecuta siempre, independientemente de haber ocurrido o no un error
finally: ### OPCIONAL
    print("La ejecucion continua")

# EXCEPCIONES POR TIPO

try:
    print("5" + 1)
# Se ejecuta si solamente ocurre un TypeError
except TypeError:
    print("Se ha producido un TypeError")
# Se ejecuta si solamente ocurre un ValueError
except ValueError as e:
    print("Se ha producido un ValueError")


## Captura de la informacion de la excepcion
try:
    print("5" + 1)
except ValueError as error:
    # Capturamos e imprimimos el objeto error
    print(error)
except Exception as error:
    # Capturamos e imprimimos el objeto error
    print(error)