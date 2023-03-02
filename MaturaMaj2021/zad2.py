with open("przyklad.txt") as file:
    ciomka = ['test']
    x = 0
    combo = 1
    memory = 0
    high = ""
    for line in file:
        data = line.split()
        ciomka.append(data[0])

        if ciomka[x] == ciomka[x+1]:
            combo += 1
        else:
            if combo > memory:
                high = ciomka[x]
                memory = combo
            combo = 1
        x += 1

    print(high,",", "długość ciągu -", memory)



