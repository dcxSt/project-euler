import numpy as np
from CheckPrime import checkPrime

# load the big list of primes all primes below 10^8
primes = np.load('primes_below_50000000.npy')

# find the largest prime that is smaller than the square root
count=0
while True:
    b = 10**4 - 1 - 2*count
    if checkPrime(b):
        p = b
        break
    count+=1

index = list(primes).index(p)

larger_primes = list(primes[index+1:])
smaller_primes = primes[:index+1][::-1]# reverses the array


# total
total=0
# l is the number of primes that find themselves between
l = 0
for i in smaller_primes:
    l+=1# +1 for the smaller prime that was added
    j=0
    count = 0
    k = larger_primes[0]
    while k*i < 10**8: 
        j+=1
        try: larger_primes = larger_primes[1:]
        except: break
        k = larger_primes[0]
    l+=j
    larger_primes = larger_primes[j:]
    total+=l


print('total',total)

