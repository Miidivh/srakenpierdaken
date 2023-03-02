# Sprawdź jaka jest najmniejsza i największa  różnica między kolejnymi liczbami

with open('plik.txt') as file:
    number = []
    difference = []
    for line in file:
        data = line.split()

        data = [int(num) for num in data if num.isdigit()]

        number.append(data)

    for z in range(13):
        y = z + 1
        x = (number[z][0] - number[y][0])

        difference.append(abs(x))
    difference.sort()
    print("Biggest difference: ", difference[-1])
    print("Smallest difference: ", difference[0])
