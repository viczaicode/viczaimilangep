def feladat1():
    print("I/A:")
    ertekeles:int = 999
    while not (ertekeles >=1 and ertekeles <= 20):
        muzeum_nev:str = str(input("Múzeum neve: "))
        nev:str = str(input("Látogató neve: "))
        ertekeles:int = int(input("Értékelés (1-20): "))
        if ertekeles <= 0:
            print("Az értékelés nem lehet negatív vagy 0!")
        elif ertekeles > 20:
            print("20 pont feletti értékelés nem elfogadható")
        else:
            print("I/B:")
            print("Köszönjük az értékelést!\n")
        
