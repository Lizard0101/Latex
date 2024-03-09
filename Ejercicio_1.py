def suma(a, b):
    """Calcula la suma de dos números."""
    return a + b


def resta(a, b):
    """Calcula la resta de dos números."""
    return a - b


def multiplicacion(a, b):
    """Calcula la multiplicación de dos números."""
    return a * b


def division(a, b):
    """
    Calcula la división de dos números.

    Si el segundo número es cero, retorna un mensaje de error.
    """
    if b == 0:
        return "Error: No se puede dividir entre cero."
    else:
        return a / b


def main():
    """
    Función principal del programa.

    Solicita al usuario que ingrese dos números,
    luego realiza operaciones matemáticas básicas
    (suma, resta, multiplicación y división)
    e imprime los resultados.
    """
    # Solicitar al usuario que ingrese dos números
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: Ingrese solo números válidos.")
        return

    # Realizar operaciones matemáticas
    resultado_suma = suma(num1, num2)
    resultado_resta = resta(num1, num2)
    resultado_multiplicacion = multiplicacion(num1, num2)
    resultado_division = division(num1, num2)

    # Mostrar resultados
    print("Suma:", resultado_suma)
    print("Resta:", resultado_resta)
    print("Multiplicación:", resultado_multiplicacion)
    print("División:", resultado_division)


if __name__ == "__main__":
    main()
