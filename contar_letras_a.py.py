def contar_a(string):
    count = 0
    for char in string:
        if char.lower() == 'a':
            count += 1
    return count

def main():
    string = input("Informe uma string: ")
    count = contar_a(string)
    if count > 0:
        print(f"A letra 'a' ocorre {count} vezes na string.")
    else:
        print("A letra 'a' não ocorre na string.")

if __name__ == "__main__":
    main()