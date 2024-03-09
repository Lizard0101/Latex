# Solicita un número al usuario y determina si es par o impar.


def es_par(num):
    """
    Función que determina si un número es par o impar.

    Args:
    num (int): El número a verificar.

    Returns:
    str: Retorna 'par' si el número es par, 'impar' si es impar.
    """
    if num % 2 == 0:
        return "par"
    else:
        return "impar"


def main():
    """
    Función principal del programa.

    Solicita al usuario que ingrese un número,
    luego verifica si es par o impar
    e imprime el resultado.
    """
    # Solicitar al usuario que ingrese un número
    try:
        numero = int(input("Ingrese un número entero: "))
    except ValueError:
        print("Error: Por favor ingrese un número entero válido.")
        return

    # Verificar si el número es par o impar
    resultado = es_par(numero)

    # Mostrar el resultado
    print("El número ingresado es", resultado)


if __name__ == "__main__":
    main()
