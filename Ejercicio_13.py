# Generador de Tablas de Multiplicar:Crea un programa que genere la tabla de multiplicar de un número ingresado por el usuari.


def generar_tabla_multiplicar(numero):
    """
    Genera la tabla de multiplicar de un número dado.

    Args:
    numero (int): El número del cual se generará la tabla de multiplicar.

    Returns:
    list: Una lista que contiene los resultados de la tabla de multiplicar.
    """
    tabla_multiplicar = []
    for i in range(1, 11):
        resultado = numero * i
        tabla_multiplicar.append(resultado)
    return tabla_multiplicar


def main():
    """
    Función principal del programa.

    Solicita al usuario que ingrese un número,
    luego genera la tabla de multiplicar de ese número e imprime el resultado.
    """
    try:
        numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))
    except ValueError:
        print("Error: Por favor ingrese un número entero válido.")
        return

    tabla = generar_tabla_multiplicar(numero)
    print("Tabla de multiplicar de", numero, ":")
    for i, resultado in enumerate(tabla, start=1):
        print(numero, "x", i, "=", resultado)


if __name__ == "__main__":
    main()
