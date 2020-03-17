from CheckPrime import checkPrime
import numpy as np

# returns number of prime factors
def pfacs(n):
    k=0
    count=2
    while checkPrime(n)==False:
        if n%count !=0:
            count+=1
        else:
            n = int(n/count)
            k+=1
    return k+1

primes = np.load('primes_below_50000000.npy')
array = [i for i in range(4,10**8) if i not in primes]
print('checkpoint one')


def sive(array):
    count = 2
    for idx1 in range(50):
        for idx2 in range(i,60):
            count = primes[idx2]
            k = primes[idx1]*primes[idx2]*count
            while k<10**8:
                try: 
                    array.remove(k)
                except:
                    pass
                count+=1
                k = primes[idx1]*primes[idx2]*count
    return array
    
array = sive(array)

np.save('filtered_numbers.npy',array)


