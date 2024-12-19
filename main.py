import minosites
import sorozat
import helyzet

minosites.feladat1()
random_lista = sorozat.randomszamok()
szamlalo = sorozat.oszthatoak_szama(random_lista)
sorozat.konzolra_ir(szamlalo)
sorozat.fajl_ir(szamlalo)
gepek_lista = helyzet.beolvasas()
helyzet.gepek_szama(gepek_lista)
helyzet.atlag(gepek_lista)
helyzet.legkisebb(gepek_lista)