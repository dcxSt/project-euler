# sum all the first two million primes primes

from CheckPrime import checkPrime

the_sum = 5
for i in range(6,2000000,6):
    if checkPrime(i-1): the_sum+=(i-1)
    if checkPrime(i+1): the_sum+=(i+1)

print("the sum:\t",the_sum)
