# check prime class ehh... not a class...

import numpy as np

# class CheckPrime: # utility
def checkPrime(n): # boolean - true if prime
    # @ staticmethods
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    for i in range(3,int(np.sqrt(n)+1),2):
        if n%i == 0:
            return False
    return True
