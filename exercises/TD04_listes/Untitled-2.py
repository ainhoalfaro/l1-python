l = [0,1,2,3,4,5]
n = 2


def fonction (l,n):
    somme = 0
    for i in range (len(l)):
        if  i > n :
            somme += 1
    return somme 
print (fonction(l,n)) 


base = [[200, -42, 312],[-51, -22, -3, 80,23]]

liste = [1,2,3,4]

def bilan_mensuel(L):
    sommeNegatif = 0 
    sommePositif = 0 
    l = [0]
    l2 = [0]
    l3 = [0]
    for i in L:
        for j in  i : 
            if j > 0:
                sommePositif += j 
                l.append(sommePositif)
            else: 
                sommeNegatif += j
                l2.append(sommeNegatif)
    return l3.extend[[l , l2]]

print(bilan_mensuel(base))

base = [[200, -42, 312],
[-51, -22, -3, 80,23]]

def bilan_mensuel(l):
    sommeNegatif: 0 
    sommePositif: 0 
    for i in range(len(l)):
        for j in range(len(l)): 
            if j > 0:
                sommePositif += j 
            else: 
                sommeNegatif += j
    return print("Le total de dépenses est", sommeNegatif, "et le total des rentrées est", sommePositif)

print(bilan_mensuel(base))



mois = 8 

def bilan_final(L):
    bilanfinal = 0 
    for i in range(mois):
        bilanfinal += bilan_mensuel(L)
    return ("Le bilan final est", bilanfinal)

print(bilan_final(base))