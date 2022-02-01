# distinct primes factors
import numpy as np

def checkprime(k:int):
    # assumes k positive bigger than one
    if k == 2:
        return True,k
    if k == 3:
        return True,k
    if k % 2 == 0:
        return False, 2
    for i in range(3,int(np.sqrt(k)+2),2):
        if k % i == 0:
            return False,i
    return True,k


def factor(n):
    factors = []
    isprime,factor = checkprime(n)
    factors.append(factor)
    while not isprime:
        n = n // factor
        isprime,factor = checkprime(n)
        factors.append(factor)
    return factors



n = 2
counter = 1
blip = 0 # silly variable
while True:
    n += 1
    factors = factor(n)
    if len(set(factors)) == 4:
        counter += 1
        # print(f"n={n} {set(factors)}")
        for i in range(1,4):
            factors = factor(n + i)
            if len(set(factors)) != 4:
                n += i - 1
                break
            elif i==3:
                print("halleluja!")
                print(f"\n\nn={n} {factor(n)}")
                print(f"n={n+1} {factor(n+1)}")
                print(f"n={n+2} {factor(n+2)}")
                print(f"n={n+3} {factor(n+3)}")
                input("[Enter] to exit")
            counter += 1


    if counter % 10**5 == 0:
        if blip != counter:
            blip = counter
            print(f"{counter} n={n - 1} {factor(n-1)}")


print(n)
