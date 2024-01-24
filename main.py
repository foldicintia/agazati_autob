import jelszo
import oszthato
import autom

"""
print("I.feladat")
jelszo.bekeres()


print("II.feladat")
lista = oszthato.random_sz()
print(f"\tA lista: {lista}")

db = oszthato.ottel_oszthato(lista)
print(f"\tA héttel osztható számok száma: {db}")
"""

print("III.feladat")
kocsi = autom.beolvas()

print("III/TÁBLA:")
autom.tabla(kocsi[3])
autom.kiiras(kocsi[3])

print("III/FLOTTA:")
autom.flotta(kocsi)

print("III/ÉRTÉKES:")
legfiatalabb_index=autom.ertekes(kocsi)
print(f"\tA legfiatalabb autó: {kocsi[legfiatalabb_index].nev}({kocsi[legfiatalabb_index].ev})")