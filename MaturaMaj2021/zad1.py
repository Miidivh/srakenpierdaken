with open("instrukcje.txt") as file:
    long = 0
    for line in file:
        data = line.split()

        if data[0] == "DOPISZ":
            long += 1
        elif data[0] == "USUN":
            long -= 1

    print(long)
