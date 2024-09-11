def pertence_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num

def main():
    num = int(input("Informe um número: "))
    if pertence_fibonacci(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} NÃO pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()