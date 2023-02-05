# Pobierz ostatnią literę z każdej linijki i podaj tą, która jest ostatnia w alfabecie

with open('plik.txt') as file:
    lastChar = []
    for line in file:
        data = line.split()

        letters = ''.join(lit for lit in data if lit.isalpha())

        lastChar.append(letters[-1])

        lastChar.sort(reverse=True)

print("List of last letters: ", lastChar)
print("Last letter alphabetically is: ", lastChar[0])
