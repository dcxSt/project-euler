import numpy as np

def isprime(n):
    if n==2:return True
    if n==3:return True
    if n%2==0: return False
    for i in range(3,int(np.sqrt(n)+1),2):
        if n%i==0: return False
    return True 

def check_circ(n):
    if "0" in str(n): return False
    perms = [int(str(n)[k:]+str(n)[:k]) for k in range(len(str(n)))]
    for i in perms:
        if not isprime(i):
            return False
    return True

s = 0
for i in range(2,10**6):
    if check_circ(i):
        s += 1
        print(i)

print()
print("s = {}".format(s))
