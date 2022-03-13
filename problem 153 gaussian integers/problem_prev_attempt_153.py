#!/usr/bin/python3 

# problem 153 try 3
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pickle


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

# same as below with no duplicates
def pfactors_no_dup(n):
    for p in primes(n):
        first=True
        while n%p==0:
            if first==True:
                yield p
                first=False
            n=n//p
            if n==1: return

def pfactors_no_dup_and_n(n):
    for p in primes(n):
        first=True
        while n%p==0:
            if first==True:
                yield p
                first=False
            n=n//p
            if n==1: return
    yield n
        


# returns prime factors bigger than 1 and smaller or eq to n
def pfactors(n):
    for p in primes(n):
        while n%p==0:
            yield p
            n=n//p
            if n==1: return


def natural_factors_sum(n=10**5):
    return sum([k*(n//k) for k in range(1,n+1)])

def get_r(z_over_n):
    r=z_over_n
    if r-1/2<0: return 1-4*(1/2-r)
    # otherwize it is bibber than 1/2
    return 2*r-1
    #print("logic error in getting r")
    #raise Exception

# 2.0
def factors_sum_line2(a,b,n):
    z = a**2 + b**2 # tacitly a>b
    if z/n > 1/4:
        r = get_r(z/n)
        estimate = int((n//z) * (n/z - 0.5*r*(n//z + 1)) +0.5)# estimate
        s = sum([alpha*(n//(alpha*z)) for alpha in range(1,n//z+1)])
        if estimate != s:
            print("e",estimate)
            print("s",s)
            print("s-e",s-estimate)
            print()
        else:
            print(":):):):):):):)")
        return s
    else:
        return sum([alpha*(n//(alpha*z)) for alpha in range(1,n//z+1)])


def factors_sum_line(a,b,n):
    z = a**2 + b**2
    if a>b: return (2*a+2*b) * sum([alpha*(n//(alpha*z)) for alpha in range(1,n//z+1)])
    elif a==b: return 2*a* sum([alpha*(n//(alpha*z)) for alpha in range(1,n//z+1)])
    else: raise Exception

def main(n=10**5,start=dt.datetime.now(),times=[],keep_track=False):
    kapa = natural_factors_sum(n)
    print("natural factors' sum found")# trace
    if keep_track: times.append(dt.datetime.now())# trace

    eta = 0
    # first do the line b=1
    a,b = 1,1
    while (a**2+b**2) <= n:
        eta += factors_sum_line(a,b,n)
        a+=1
    print("line b = 1 done")# trace
    if keep_track: times.append(dt.datetime.now())# trace

    # then do the line b=2
    a,b = 3,2
    while (a**2+b**2) <= n:
        eta += factors_sum_line(a,b,n)
        a+=2
    print("line b = 2 done")# trace
    if keep_track: times.append(dt.datetime.now())# trace
    
    # then do line b=3
    a,b = 4,3
    while (a**2+b**2) <= n:
        if a%3!=0:
            eta += factors_sum_line(a,b,n)
        a+=1
    print("line b = 3 done")# trace
    if keep_track: times.append(dt.datetime.now())# trace

    # then do line b=4
    a,b = 5,4
    while (a**2+b**2) <= n:
        if a%2!=0:
            eta += factors_sum_line(a,b,n)
        a+=1
    print("line b = 4 done")# trace
    if keep_track: times.append(dt.datetime.now())# trace

    # you get the picture now do all the odds
    a,b = 6,5
    while (a**2+b**2) <= n:
        if b%21==0:
            print("line b =",b,"done ;",end="\t")# trace
            if keep_track: times.append(dt.datetime.now())# trace
        while (a**2+b**2) <= n:
            if all([a%i!=0 for i in pfactors_no_dup(b)]) and a%b!=0:
                eta += factors_sum_line(a,b,n)
            a+=1
        b+=2
        a=b+1

    # if b is even no even a will be good
    a,b = 7,6
    while (a**2+b**2) <= n:
        if b%20==0:
            print("line b =",b,"done ;",end="\t")# trace
            if keep_track: times.append(dt.datetime.now())# trace
        while (a**2+b**2) <= n:
            if all([a%i!=0 for i in pfactors_no_dup(b)]) and a%b!=0:
                eta += factors_sum_line(a,b,n)
            a+=2
        b+=2
        a=b+1

    gamma = kapa + eta
    return gamma,times

times = []

start = dt.datetime.now()
times.append(start)

n=10**5
gamma,times = main(n,start=start,times=times)
f = open("the_answer.txt","w")
f.write(str(n))
f.close()

print("\n\ngamma =",gamma)

times.append(dt.datetime.now())

print("\nrun-time :",times[-1] - start)

