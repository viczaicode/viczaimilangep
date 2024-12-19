from Helyzetek import Helyzet

def beolvasas():
    gepek_lista=[]
    fajlom = open("gep.txt", "r", encoding="UTF-8")
    elso_sor = fajlom.readline()
    sorok_lista = fajlom.readlines()
    for i in range(0, len(sorok_lista), 1):
        sor = sorok_lista[i].strip()
        sor_lista = sor.split("!")
        gep = Helyzet(sor_lista[0], sor_lista[1], sor_lista[2], sor_lista[3])
        gepek_lista.append(gep)
    fajlom.close()
    return gepek_lista

def gepek_szama(gepek_lista):
    gepek = len(gepek_lista)
    print("III/A,B:")
    print(f"A gépek száma: {gepek}.\n")

def atlag(gepek_lista):
    oszto:int = 0
    osszeg:int = 0
    for i in range(0, len(gepek_lista), 1):
        if gepek_lista[i].id % 2 == 0:
            osszeg += gepek_lista[i].id
            oszto += 1
    atlag:float = osszeg / oszto
    print("III/C:")
    print(f"A páros teremszámú termek azonosító átlaga: {atlag}.\n")

def legkisebb(gepek_lista):
    legkisebb:int = 100
    for i in range(0, len(gepek_lista), 1):
        if gepek_lista[i].tipus == "asztali":
            legkisebb_hely = gepek_lista[i].hely
            if gepek_lista[i].id < legkisebb:
                legkisebb = gepek_lista[i].id
    print("III/D:")
    print(f"A legkisebb asztali gép azonosítója: {legkisebb}, helye: {legkisebb_hely}.\n")
