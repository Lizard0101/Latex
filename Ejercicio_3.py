"""Área de un Triángulo:
-Pide la base y la altura de un triángulo al usuario y calcula su área. """


def calcular_area_triangulo(base, altura):
    """
    Función que calcula el área de un triángulo.

    Args:
    base (float): La longitud de la base del triángulo.
    altura (float): La altura del triángulo.

    Returns:
    float: El área del triángulo.
    """
    area = (base * altura) / 2
    return area


def main():
    """
    Función principal del programa.

    Solicita al usuario que ingrese la base y la altura del triángulo,
    luego calcula el área del triángulo e imprime el resultado.
    """
    # Solicitar al usuario que ingrese la base y la altura del triángulo
    try:
        base = float(input("Ingrese la longitud de la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")
        return

    # Verificar que la base y la altura sean positivas
    if base <= 0 or altura <= 0:
        print("Error: La base y la altura deben ser valores positivos.")
        return

    # Calcular el área del triángulo
    area = calcular_area_triangulo(base, altura)

    # Mostrar el resultado
    print("El área del triángulo es:", area)


if __name__ == "__main__":
    main()
