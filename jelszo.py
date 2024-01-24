def bekeres():
    felhasznalo_nev = input("Add meg a felhasználóneved!: ")
    jelszo = input("Add meg a jelszavad!: ")
    i=1
    while not (felhasznalo_nev == "bori99" and jelszo == "Szivecske>3"):
        print("\tBelépés megtagadva.")
        felhasznalo_nev = input("Add meg a felhasználóneved!: ")
        jelszo = input("Add meg a jelszavad!: ")
        i+=1
    print("\tBelépés engedélyezve.")
