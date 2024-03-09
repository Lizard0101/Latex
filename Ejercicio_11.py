# Ordenamiento de Lista:
# Ordena una lista de números ingresados por el usuario de menor a mayor.


def ordenar_lista(lista):
    """
    Ordena una lista de números de menor a mayor.

    Args:
    lista (list): La lista de números a ordenar.

    Returns:
    list: La lista ordenada de menor a mayor.
    """
    return sorted(lista)


def main():
    """
    Función principal del programa.

    Solicita al usuario que ingrese una lista de números,
    luego ordena la lista de menor a mayor e imprime el resultado.
    """
    try:
        numeros = input("Ingrese una lista de números separados por espacios: ").split()
        numeros = [float(numero) for numero in numeros]
    except ValueError:
        print("Error: Por favor ingrese solo números válidos.")
        return

    lista_ordenada = ordenar_lista(numeros)
    print("La lista ordenada de menor a mayor es:", lista_ordenada)


if __name__ == "__main__":
    main()
