# Palíndromo:
# Verifica si una palabra ingresada por el usuario es un palíndromo.


def es_palindromo(palabra):
    """
    Verifica si una palabra dada es un palíndromo.

    Args:
    palabra (str): La palabra a verificar.

    Returns:
    bool: True si la palabra es un palíndromo, False de lo contrario.
    """
    # Eliminar espacios y convertir a minúsculas para simplificar la comparación
    palabra = palabra.replace(" ", "").lower()
    # Verificar si la palabra es igual a su inversa
    return palabra == palabra[::-1]


def main():
    """
    Función principal del programa.

    Solicita al usuario que ingrese una palabra,
    luego verifica si es un palíndromo e imprime el resultado.
    """
    palabra = input("Ingrese una palabra para verificar si es un palíndromo: ")
    if es_palindromo(palabra):
        print("¡La palabra '{}' es un palíndromo!".format(palabra))
    else:
        print("La palabra '{}' no es un palíndromo.".format(palabra))


if __name__ == "__main__":
    main()
