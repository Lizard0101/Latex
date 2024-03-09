# Números de la Serie Fibonacci:
# Genera los primeros 10 números de la serie Fibonacci.


def fibonacci(n):
    """
    Genera los primeros n números de la serie Fibonacci.

    Args:
    n (int): El número de términos de la serie Fibonacci a generar.

    Returns:
    list: Una lista que contiene los primeros n números de la serie Fibonacci.
    """
    # Inicializar la lista con los primeros dos términos de la serie
    fibonacci_series = [0, 1]
    # Generar los siguientes términos de la serie hasta alcanzar n términos
    for i in range(2, n):
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_term)
    return fibonacci_series


def main():
    """
    Función principal del programa.

    Genera los primeros 10 números de la serie Fibonacci e imprime el resultado.
    """
    n = 10  # Número de términos de la serie Fibonacci a generar
    fibonacci_numbers = fibonacci(n)
    print("Los primeros {} números de la serie Fibonacci son:".format(n))
    print(fibonacci_numbers)


if __name__ == "__main__":
    main()
