# Inversión de Cadena:
# Toma una cadena de texto y muestra su inversión.


def invertir_cadena(cadena):
    """
    Invierte una cadena de texto.

    Args:
    cadena (str): La cadena de texto a invertir.

    Returns:
    str: La cadena invertida.
    """
    return cadena[::-1]


def main():
    """
    Función principal del programa.

    Solicita al usuario que ingrese una cadena de texto,
    luego invierte la cadena e imprime el resultado.
    """
    cadena = input("Ingrese una cadena de texto: ")
    cadena_invertida = invertir_cadena(cadena)
    print("La cadena invertida es:", cadena_invertida)


if __name__ == "__main__":
    main()
