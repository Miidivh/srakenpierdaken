with open("instrukcje.txt") as file:
    ciomka = ['test']
    for line in file:
        data = line.split()

        if data[0] == "DOPISZ":
            ciomka.append(data[1])

    number = (ciomka.count(i) for i in ciomka)
    most_frequent = max(set(ciomka), key=ciomka.count)
    print(most_frequent, max(number))
