with open('przyklad.txt') as file:
    x = 0
    liczby = []
    for line in file:
        data = line.split()

        if data[0][0] == data[0][-1]:
            x += 1
            liczby.append(data)

    print(liczby[0], x)
