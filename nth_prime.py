# just a bog standard prime finder
import numpy as np

# returns False if composite
def is_prime(n):
    for i in range(3,int(np.sqrt(n)+1),2):
        if float(n)/i == int(float(n)/i):
            return False
    return True

# tells you what the n'th prime is
def main(n):
    count = 2# the first one is 2, the second is 3
    k = 3
    while count < n:
        k+=2
        if is_prime(k):
            count+=1

    print("the",n,"th prime is",k)

main(int(input("number:")))
