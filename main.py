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
autom.tabla(kocsi[3])
autom.kiiras(kocsi[3])

autom.flotta(kocsi)

legfiatalabb_index=autom.ertekes(kocsi)
print(f"A legfiatalabb autó: {kocsi[legfiatalabb_index].nev}({kocsi[legfiatalabb_index].ev})")