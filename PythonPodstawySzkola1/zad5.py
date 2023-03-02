# Pobierz wyrazy i zaszyfruj je krok=5

with open('plik.txt') as file:
    number = []
    key = 5
    for line in file:
        data = line.split()

        letters = ''.join(lit for lit in data if lit.isalpha())

        for i in range(len(letters)):
            y = ord(letters[i]) + key
            number.append(chr(y))

        print("Cyphered numbers: ", ''.join(number))
        number.clear()

