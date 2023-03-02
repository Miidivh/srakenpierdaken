lista = ""

def dopisz(lista, litera):
    lista += litera
    return lista

def usun(lista):
    lista = lista[:-1]
    return lista

def zmien(lista, litera):
    lista[-1] = litera
    return "".join(lista)

def przesun(litera, instrukcja):
    for i in range(len(instrukcja)):
        if instrukcja[i] == litera:
            if instrukcja[i] == 'Z':
                instrukcja[i] = 'A'
            else:
                instrukcja[i] = chr(ord(instrukcja[i]) + 1)
            break
    return "".join(instrukcja)


with open("instrukcje.txt") as file:
    for line in file:
        data = line.split()

        if data[0] == "DOPISZ":
            lista = dopisz(lista, data[1])

        elif data[0] == "USUN":
            lista = usun(lista)

        elif data[0] == "PRZESUN":
            lista = przesun(data[1], list(lista))

        elif data[0] == "ZMIEN":
            lista = zmien(list(lista), data[1])

    print(lista)
