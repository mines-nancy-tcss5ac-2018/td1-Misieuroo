def tri():
    f=open('names.txt','r')
    chaine=f.read()
    n=len(chaine)
    chaine_mieux=chaine[1:n-1]
    L=chaine_mieux.split('","')
    return sorted(L)

def score(mot):
    somme=0
    for lettre in mot:
        somme+=ord(lettre)-64
    return somme

assert score('COLIN')==53

def total():
    somme=0
    L=tri()
    n=len(L)
    for i in range(n):
        somme+=(i+1)*score(L[i])
    return somme

print(total())