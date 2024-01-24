import random

def random_sz():
    szamok=[]
    for i in range(0,50,1):
        szam = random.randint(1,100)
        szamok.append(szam)
    return szamok

def ottel_oszthato(lista):
    db = 0
    for i in range(0,len(lista),1):
        if lista[i] % 7 == 0:
            db+=1
    return db