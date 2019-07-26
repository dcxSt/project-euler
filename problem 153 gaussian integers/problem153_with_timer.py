#!/usr/bin/python3 

# problem 153 try 3
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pickle


# yilds numbers which are relatively prime to b and such that a**2 + b**2 <= n
def relatively_primes(b,n):
    pfac = [i for i in pfactors_no_dup_and_n(b)]
    yield b+1
    for i in range(b+2,int(np.sqrt(n-b**2)+1)):
        if not any([i%j==0 for j in pfac]): yield i
        
# almost same as above but assumes b is even (to make it run faster)
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

def get_r(z_over_n):
    r=z_over_n
    if r-1/2<0: return 1-4*(1/2-r)
    # otherwize it is bibber than 1/2
    return 2*r-1
    #print("logic error in getting r")
    #raise Exception

# assumes a>b
# returns sum of gaussian factors that can be found on the lines that passing through the origin
# and through the points a+ib ; a-ib ; b+ia ; b-ia
def factors_sum_line(a,b,n):
    z = a**2 + b**2
    if a>b: return (2*a+2*b) * sum([alpha*(n//(alpha*z)) for alpha in range(1,n//z+1)])
    elif a==b: return 2*a* sum([alpha*(n//(alpha*z)) for alpha in range(1,n//z+1)])
    else: raise Exception


def main(n,times): 
    times.append([0.5,dt.datetime.now()])
    kapa = natural_factors_sum(n)
    print("natural factors' sum found:",kapa)# trace
    times.append([0.5,dt.datetime.now()])# trace

    eta = 0
    # first do the line b=1
    b = 1
    times.append([b,dt.datetime.now()])# trace
    for a in range(1,int(np.sqrt(n-1)+1)):
        eta += factors_sum_line(a,b,n)
    print("line b = 1 done")# trace
    times.append([b,dt.datetime.now()])# trace


    # do all the odds
    for b in range(3,int(0.5*(np.sqrt(2*n-1)-1))+1,2):
        if b%25==0:
            print("line b =",b,"done ;",end="\t")# trace
        
        times.append([b,dt.datetime.now()])# trace
        for a in relatively_primes(b,n): eta += factors_sum_line(a,b,n)
        times.append([b,dt.datetime.now()])# trace


    # if b is even no even a will be good
    for b in range(2,int(0.5*(np.sqrt(2*n-1)-1)+1),2):
        if b%50==0:
            print("line b =",b,"done ;",end="\t")# trace
        times.append([b,dt.datetime.now()])# trace
        for a in relatively_primes_even(b,n): eta += factors_sum_line(a,b,n)
        times.append([b,dt.datetime.now()])# trace

    gamma = kapa + eta
    return gamma,times

times = []

start = dt.datetime.now()
times.append([0,start])

n=10**8
gamma,times = main(n,times=times)

print("\n\ngamma =",gamma)

times.append([times[-1][0]+1,dt.datetime.now()])
t = open("times.pickle","wb")
pickle.dump(times,t)
t.close()

print("\nrun-time :",times[-1][1] - start)

