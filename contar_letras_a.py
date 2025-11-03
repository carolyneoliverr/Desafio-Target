def contar_a(string: str) -> int:
    """
    Conta o numero de letras 'a' (maiusculas ou minusculas) em uma string.
    """
    count = 0
    for char in string:
        if char.lower() == 'a':
            count += 1
    return count


def main():
    texto = input("Informe uma string: ")
    quantidade = contar_a(texto)
    if quantidade > 0:
        print(f"A letra 'a' ocorre {quantidade} vezes na string.")
    else:
        print("A letra 'a' nao ocorre na string.")


if __name__ == "__main__":
    main()
