# truncatable primes
import numpy as np

def check_prime(n): # assumes positive integer
    if n == 1:return False
    if n == 2:return True
    if n % 2 == 0:return False
    if n == 3:return True
    for i in range(3,int(np.sqrt(n)+2),2):
        if n % i == 0: return False
    return True 

def check_truncatable(p):
    if not check_prime(p):return False
    if len(str(p)) == 1:return True
    if "0" in str(p):return False 
    for i in range(1,len(str(p))):
        if not check_prime(int(str(p)[i:])):return False
        if not check_prime(int(str(p)[:-i])):return False
    return True

count = 0
n = 10
tps = [] # list of truncatable primes
while True:
    if check_truncatable(n):
        tps.append(n)
        count += 1
        if count == 11:print("\nHURRAY THE SEARCH IS DONE, SUPPOSEDLY\n")
        print("the prime {} is truncatable\n{} tps have been found: {}".format(n,count,tps))
        print("their sum is {}".format(sum(tps)))


    n += 1

