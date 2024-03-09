# Lista de Cuadrados:
# Crea una lista de los cuadrados de los primeros 10 números naturales.


def lista_cuadrados():
    """
    Crea una lista de los cuadrados de los primeros 10 números naturales.

    Returns:
    list: Una lista de los cuadrados de los primeros 10 números naturales.
    """
    cuadrados = [i**2 for i in range(1, 11)]
    return cuadrados


def main():
    """
    Función principal del programa.

    Crea la lista de los cuadrados de los primeros 10 números naturales
    e imprime la lista resultante.
    """
    cuadrados = lista_cuadrados()
    print("Lista de cuadrados de los primeros 10 números naturales:", cuadrados)


if __name__ == "__main__":
    main()
