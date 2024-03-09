# Contador de Vocales:
# Cuenta el número de vocales en una cadena de texto.


def contar_vocales(cadena):
    """
    Cuenta el número de vocales en una cadena de texto.

    Args:
    cadena (str): La cadena de texto en la que se contarán las vocales.

    Returns:
    int: El número de vocales en la cadena de texto.
    """
    # Convertir la cadena a minúsculas para hacer la comparación de manera más sencilla
    cadena = cadena.lower()
    # Inicializar el contador de vocales
    contador_vocales = 0
    # Definir las vocales
    vocales = "aeiou"
    # Iterar sobre cada caracter en la cadena
    for caracter in cadena:
        # Verificar si el caracter es una vocal
        if caracter in vocales:
            contador_vocales += 1
    return contador_vocales


def main():
    """
    Función principal del programa.

    Solicita al usuario que ingrese una cadena de texto,
    luego cuenta el número de vocales en la cadena e imprime el resultado.
    """
    cadena = input("Ingrese una cadena de texto: ")
    numero_vocales = contar_vocales(cadena)
    print("El número de vocales en la cadena es:", numero_vocales)


if __name__ == "__main__":
    main()
