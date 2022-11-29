n = 3 
[3, 10, 5, 16, 8, 4, 2, 1]

def syracuse(n):
    l= [n]
    while n > 1: 
        if n%2 == 0 :
            n = n// 2 
        else:
            n = 3 * n + 1 
        l.append(n)
    return l
print(syracuse(3))


def testeConjecture(n_max):
    for i in range(1, n-max+1):
        syracuse(i)
    return True 

print(testeConjecture(10000))

def tempsVol(n):
    l = syracuse(n)
    return len(l)-1

print("Le temps de vol de", 3, "est", tempsVol(3))

def tempsVolListe(n_max):
    return [tempsVol(i)for i in range (1, n-max+1)]

print(tempsVolListe(100))

listeVol = tempsVolListe(10000)
tpsMax = max (listeVol)
entier_Max = listeVol.index(tpsMax)+1

def altMax (n):
    l= syracuse(n)
    return max(l)
listeAlt= [altMax(i) for i in range(1,10001)]
altMaxliste= max(listeAlt)
entierMax = listeAlt.index(altMaxliste)+1

carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5,11, 10, 8],[16, 2, 3, 13]]

carre_mag[0][1]

carre_pas_mag = [list(l) for l in carre_mag]
carre_pas_mag[3][2] = 7 