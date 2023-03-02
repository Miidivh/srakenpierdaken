def rozloz(n):
    czynniki = []
    k = 2
    while n != 1 and k * k <= n:
        while n % k == 0:
            czynniki.append(k)
            n //= k
        k += 1

    return czynniki


max_czynnikow = -1
max_czynnikow_liczba = -1
max_roznych_czynnikow = -1
max_roznych_czynnikow_liczba = -1


with open('przyklad.txt') as file:
    for line in file:
        liczba = int(line)
        rozklad = rozloz(liczba)

        if len(rozklad) > max_czynnikow:
            max_czynnikow = len(rozklad)
            max_czynnikow_liczba = liczba

        rozne = set(rozklad)
        if len(rozne) > max_roznych_czynnikow:
            max_roznych_czynnikow = len(rozne)
            max_roznych_czynnikow_liczba = liczba

    print(max_czynnikow_liczba, max_czynnikow, max_roznych_czynnikow_liczba, max_roznych_czynnikow)
