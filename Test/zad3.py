# Sprawdź, który z wyrazów ma najwięcej różnych liter.

with open('plik.txt') as file:
    highest_number = []
    longest_word = ""
    list1 = []
    for line in file:
        data = line.split()

        letters = ''.join(lit for lit in data if lit.isalpha())

        unique_characters = set(letters)

        number_characters = len(unique_characters)

        highest_number.append(number_characters)

        longest_word = ''.join(unique_characters)

        list1.append(longest_word)

    print("Phrase with most letters: ", max(list1, key=len))
    print("Number of letters in phrase: ", max(highest_number))

