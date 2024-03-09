# Suma de Números Pares:
# Calcula la suma de los números pares en un rango especificado por el usuario.


def suma_numeros_pares(inicio, fin):
    """
    Calcula la suma de los números pares en un rango dado.

    Args:
    inicio (int): El inicio del rango.
    fin (int): El fin del rango.

    Returns:
    int: La suma de los números pares en el rango dado.
    """
    suma = 0
    for num in range(inicio, fin + 1):
        if num % 2 == 0:
            suma += num
    return suma


def main():
    """
    Función principal del programa.

    Solicita al usuario que ingrese el inicio y el fin del rango,
    luego calcula la suma de los números pares en ese rango e imprime el resultado.
    """
    try:
        inicio = int(input("Ingrese el inicio del rango: "))
        fin = int(input("Ingrese el fin del rango: "))
    except ValueError:
        print("Error: Por favor ingrese números enteros válidos.")
        return

    if inicio > fin:
        print("Error: El inicio del rango debe ser menor o igual que el fin del rango.")
        return

    suma_pares = suma_numeros_pares(inicio, fin)
    print(
        "La suma de los números pares en el rango [{}, {}] es: {}".format(
            inicio, fin, suma_pares
        )
    )


if __name__ == "__main__":
    main()
