# Wyświetl wszystkie parzyste liczby.

with open('plik.txt') as file:
    number = []
    for line in file:
        data = line.split()

        data = [int(num) for num in data if num.isdigit()]

        if (data[0]) % 2 == 0:
            print("Even number: ", data)
