plik = open('przyklad.txt')
wiersze = plik.readlines()
def how_many_good_3(wiersze):
    trojki = []

    for first in range(len(wiersze)):
        first_number = int(wiersze[first])

        for second in range(len(wiersze)):
            if first == second:
                continue
            else:
                second_number = int(wiersze[second])

            if second_number % first_number == 0:
                for third in range(len(wiersze)):
                    if first == third or second == third:
                        continue
                    else:
                        third_number = int(wiersze[third])

                    if third_number % second_number == 0:
                        trojki.append([first_number, second_number, third_number])

    return trojki


good_3 = how_many_good_3(wiersze)
print(len(good_3))
for trojka in good_3:
    print(trojka)
