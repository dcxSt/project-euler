import numpy as np

# THIS METHOD TAKES TOO MUCH MEMORY
#primes = [i for i in range(3,10**9,2)]
#primes = np.array(primes)
#print("Primes List Calculated!")
#
#
#for i in range(3,int(np.sqrt(10**9)+2),2):
#    modarr = primes % i
#    idxs = np.where(modarr==0)[0]
#    if len(idxs) > 0:
#        if primes[idxs[0]] == i and len(idxs) > 1:
#            idxs = idxs[1:]
#        if len(idxs) > 0:
#            primes = np.delete(primes, idxs) 

def is_pandigital(n):
    if "0" in str(n):
        return False # i'm not sure if it's right to exclude zeros
    for i in range(1,len(str(n))+1):
        if str(i) not in str(n):
            return False
    return True

def is_prime(n):
    if n%2==0:return False
    for i in range(3,int(np.sqrt(n)+2),2):
        if n%i==0:return False
    return True

for p in range(10**9,1,-1):
    if is_pandigital(p):
        print("{}".format(p),end=" ")
        if is_prime(p):
            print("\n\nThe largest n-digit pandigital prime is {}".format(p))
            break 

print("\nEnd")


