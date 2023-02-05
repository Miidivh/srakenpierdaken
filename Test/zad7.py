# Zamień wszystkie litery na liczby (ASCII) i podaj wartość sumaryczną w każdym wierszu.

with open('plik.txt') as file:
    number = []
    for line in file:
        data = line.split()

        letters = ''.join(lit for lit in data if lit.isalpha())

        for i in range(len(letters)):
            y = ord(letters[i])
            number.append(y)
        print("Cumulative value of ASCII in line: ", sum(number))
        number.clear()
