import random

def randomszamok():
    print("II/A,B,C:")
    i:int=1
    random_lista=[]
    while i <= 15:
        szam:int = random.randint(-90,500)
        random_lista.append(szam)
        if i < 15:
            print(szam, end="*")
            i += 1
        if i == 15:
            print(f"{szam}\n")
            i += 1
    return random_lista

def oszthatoak_szama(random_lista):
    szamlalo:int= 0
    for i in range(0, len(random_lista), 1):
        if (random_lista[i] % 10 == 0):
            szamlalo += 1
    return szamlalo

def konzolra_ir(szamlalo):
    print("II/D, E:")
    print(f"Tízzel oszthatóak száma: {szamlalo}.\n")

def fajl_ir(szamlalo):
    kiirando:str = str(szamlalo)
    fajlom = open("kimutatas.txt", "w", encoding="UTF-8")
    fajlom.write(kiirando)