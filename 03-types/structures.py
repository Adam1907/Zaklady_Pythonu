def pismenaPocet():
    veta = input("Věta:")
    vyskyt = {}
    vyskyt2 = []

    for i in veta:
        if i in vyskyt:
            vyskyt[i] += 1
        else:
            vyskyt[i] = 1

    for i in vyskyt:
        tpl = (i, vyskyt[i])
        vyskyt2.append(tpl)

    print(""+ str(vyskyt2))


pismenaPocet()