def miroir(n):
    return int(str(n)[::-1])

def iteration(n):
    return n+miroir(n)

def lychrel_check(n):
    x=n+miroir(n)
    for i in range(50):
       if x==miroir(x):
           return False
       else:
           x=iteration(x)
    return True

assert not(lychrel_check(47))
assert not(lychrel_check(349))

def comptage():
    compteur=0
    for i in range(1,10001):
        if lychrel_check(i):
            compteur+=1
    return compteur

print(comptage())