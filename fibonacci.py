def pertence_fibonacci(num: int) -> bool:
    """
    Verifica se um numero pertence a sequencia de Fibonacci.
    Retorna True se pertence, False caso contrario.
    """
    if num < 0:
        return False
    if num in (0, 1):
        return True
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num


def main():
    try:
        num = int(input("Informe um numero: "))
        if pertence_fibonacci(num):
            print(f"O numero {num} pertence a sequencia de Fibonacci.")
        else:
            print(f"O numero {num} NAO pertence a sequencia de Fibonacci.")
    except ValueError:
        print("Entrada invalida. Por favor, informe um numero inteiro.")


if __name__ == "__main__":
    main()
