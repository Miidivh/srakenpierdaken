# Znajdź największą i najmniejszą liczbę

with open('plik.txt') as file:
    number = []
    for line in file:
        data = line.split()

        data = [int(num) for num in data if num.isdigit()]

        number.append(data)

print("Highest number:", max(number))
print("Lowest number:", min(number))

