# Número Primo:
# Verifica si un número ingresado por el usuario es primo o no.


def es_primo(numero):
    """
    Verifica si un número dado es primo o no.

    Args:
    numero (int): El número a verificar.

    Returns:
    bool: True si el número es primo, False de lo contrario.
    """
    # Un número menor o igual que 1 no es primo
    if numero <= 1:
        return False
    # Verificar si el número es divisible por algún número entre 2 y su raíz cuadrada
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def main():
    """
    Función principal del programa.

    Solicita al usuario que ingrese un número,
    luego verifica si es primo o no e imprime el resultado.
    """
    try:
        numero = int(input("Ingrese un número entero positivo mayor que 1: "))
    except ValueError:
        print("Error: Por favor ingrese un número entero válido.")
        return

    if numero <= 1:
        print("Error: El número debe ser mayor que 1.")
        return

    if es_primo(numero):
        print("El número", numero, "es primo.")
    else:
        print("El número", numero, "no es primo.")


if __name__ == "__main__":
    main()
