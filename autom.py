from Auto import Auto

def beolvas():
    kocsi=[]
    fajl=open("auto.txt","r",encoding="utf-8")
    fajl.readline()
    nyers=fajl.readlines()
    fajl.close()

    for i in range(0,len(nyers),1):
        sor=nyers[i]
        elem=sor.strip().split("$")
        nev=elem[0]
        ev=elem[1]
        auto=Auto(nev,ev)
        kocsi.append(auto)

    return kocsi

def tabla(kocsi:Auto):
    print(f"\t {kocsi.nev}: {len(kocsi.nev)} hosszú.")


def kiiras(kocsi:Auto):
    fajl=open("kiiras.txt","w",encoding="utf-8")
    fajl.write(f"\t {kocsi.nev}: {len(kocsi.nev)} hosszú.")
    fajl.close()


def flotta(kocsi):
    print(f"Az autók száma: {len(kocsi)}")


def ertekes(kocsi):
    legfiatalabb_index = 0
    for i in range(0, len(kocsi),1):
        if kocsi[i].ev > kocsi[legfiatalabb_index].ev:
            legfiatalabb_index = i
    return legfiatalabb_index