def solve(n):
    x=2**n
    somme=0
    while x>0:
        unites=x%10
        somme+=unites
        x=(x-unites)//10
    return somme

assert solve(15)==26
print(solve(1000))