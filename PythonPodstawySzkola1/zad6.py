# Znajdź wyraz, który ma taką samą pierwszą i ostatnią literę

with open('plik.txt') as file:
    for line in file:
        data = line.split()

        letters = ''.join(lit for lit in data if lit.isalpha())

        first_letter = letters[0]
        last_letter = letters[-1]

        if first_letter == last_letter:
            print("Phrase with the same first and last letter: ", letters)
