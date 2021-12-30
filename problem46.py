# Goldbach's other conjecture

"""

primes = [2]

for every odd number starting at 3:
    check to see if it's prime
    if it's prime, add it to the primes list
    if it's not prime:
        take away every single prime from it, 
            divide the remainder by two
            check if the result is a perfect square
            if it is a perfect square:
                move on to the next odd number
        return the odd number which is incompatible with Goldbach's other conjecture


"""

import numpy as np

# returns False if composite
def check_prime(n):
    if n==1: return False
    if n==2: return True
    if n==3: return True
    for i in range(3,int(np.sqrt(n)+1),2):
        if float(n)/i == int(float(n)/i):
            return False
    return True


def is_perfect_square(n):
    if np.sqrt(n) == int(np.sqrt(n)):
        return True
    return False 

primes = [2]

oddn = 3
still_searching = True

while still_searching:
    if check_prime(oddn):
        primes.append(oddn)
    else:
        contradicts_goldbach = True
        for p in primes:
            x = (oddn - p) / 2 
            if is_perfect_square(x):
                contradicts_goldbach= False 
        if contradicts_goldbach:
            print("Found it!\n{}".format(oddn)) 
            still_searching = False 
    oddn += 2

input("Bye bye [press Enter to exit]")


