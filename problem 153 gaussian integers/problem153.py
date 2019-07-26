#!/usr/bin/python3 

# problem 153
import numpy as np
import datetime as dt

# yilds numbers which are relatively prime to b and such that a**2 + b**2 <= n
def relatively_primes(b,n):
    pfac = [i for i in pfactors_no_dup_and_n(b)]
    yield b+1
    for i in range(b+2,int(np.sqrt(n-b**2)+1)):
        if not any([i%j==0 for j in pfac]): yield i
        
# same functionality as above but takes shortcuts assuming b is even (to speed it up)
def relatively_primes_even(b,n):# assumes b is even
    pfac = [i for i in pfactors_no_dup_and_n(b)][1:]
    yield b+1
    for i in range(b+3,int(np.sqrt(n-b**2)+1),2):
        if not any([i%j==0 for j in pfac]): yield i

# generates list of primes below and including n
def primes(n):
    if n < 2: return
    yield 2
    plist = [2]
    for i in range(3,n):
        test = True
        for j in plist:
            if j>n**0.5:
                break
            if i%j==0:
                test=False
                break
        if test:
            plist.append(i)
            yield i

# generates prime factors of n with no duplicates, yields nothing if n is prime
def pfactors_no_dup(n):
    for p in primes(n):
        first=True
        while n%p==0:
            if first==True:
                yield p
                first=False
            n=n//p
            if n==1: return

# generates prime factors of n with no duplicates, yields n if n is prime
def pfactors_no_dup_and_n(n):
    for p in primes(n):
        first=True
        while n%p==0:
            if first==True:
                yield p
                first=False
            n=n//p
            if n==1: return
    yield n # if it is prime only return n

# this function returns the sum of all s(n) from 1 to n where 
# s(n) := the sum of all natural prime factors of n including 1 and n
def natural_factors_sum(n=10**5):
    return sum([k*(n//k) for k in range(1,n+1)])

# assumes a>b
# returns sum of gaussian factors that can be found on the lines that passing through the origin
# and through the points a+ib ; a-ib ; b+ia ; b-ia
def factors_sum_line(a,b,n):
    z = a**2 + b**2
    if a>b: return (2*a+2*b) * sum([alpha*(n//(alpha*z)) for alpha in range(1,n//z+1)])
    elif a==b: return 2*a* sum([alpha*(n//(alpha*z)) for alpha in range(1,n//z+1)])
    else: raise Exception


def main(n=10**5,start=dt.datetime.now(),times=[],keep_track=False):
    kapa = natural_factors_sum(n)

    eta = 0
    # first do the line b=1
    for a in range(1,int(np.sqrt(n-1)+1)):
        eta += factors_sum_line(a,b=1,n=n)

    # do all the odds
    for b in range(3,int(0.5*(np.sqrt(2*n-1)-1))+1,2):
        for a in relatively_primes(b,n): eta += factors_sum_line(a,b,n)

    # if b is even no even a will be good
    for b in range(2,int(0.5*(np.sqrt(2*n-1)-1)+1),2):
        for a in relatively_primes_even(b,n): eta += factors_sum_line(a,b,n)

    gamma = kapa + eta
    return gamma


start = dt.datetime.now()

gamma = main(n=10**8)

print("\n\ngamma =",gamma)

finnish = dt.datetime.now()

print("\nrun-time :",finnish - start)

