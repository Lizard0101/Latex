# Calculadora de Factorial:
# Crea una función que calcule la factorial de un número


def factorial(numero):
    """
       Calcula el factorial de un número entero no negativo.

       Args:
    a   numero (int): El número entero del cual se calculará el factorial.

       Returns:
       int: El factorial del número dado.
    """
    # El factorial de 0 es 1
    if numero == 0:
        return 1
    # El factorial de 1 es 1
    elif numero == 1:
        return 1
    # Para números mayores que 1, calculamos el factorial iterativamente
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado


# Ejemplo de uso de la función
numero = int(input("Ingrese un número entero no negativo: "))
if numero < 0:
    print("Error: El número debe ser no negativo.")
else:
    print("El factorial de", numero, "es:", factorial(numero))
