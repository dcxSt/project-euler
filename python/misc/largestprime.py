# Project euler largest prime factor of 600851475143

import numpy as np
from operator import mul

def checkPrime(n):
    # returns true if prime
    for i in range(n):
        if i%n==0:
            return False
    return True

"""finds smallest prime that divides by that number then keeps doing 
this until the biggest one"""

def findSmallestPrime(n):
    # returns smallest prime of n
    print("n: ",n)
    if n==1:
        return 1
    elif n%2==0:
        return 2
    for i in range(3,int(n/2),2):
        if n%i==0:
            return i
    # then it is prime
    return n

def product(list):
    p=1
    for i in list:
        p*=i
    return p

startNumber = 600851475143
number = startNumber
primeFactors=[1]

while product(primeFactors)!=startNumber:
    p = findSmallestPrime(number)
    if p==1:
        print("\nERROR\n")
        break
    print(p)
    primeFactors.append(p)
    number=int(number/p)

print("\n\n",primeFactors,"\n\n",product(primeFactors),"\n",startNumber)

