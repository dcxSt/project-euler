# project euler - triangular number (2nd diagonal of pascal's)
# what is the first triangular number to have over 500 divisors

def isPrime(n):
    # returns boolean
    if n==1 or n==2 or n==3:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n/2),2):
        print(i)
        if n%i==0:
            return False
    return True

def primeFactors(n):
    # returns list of non-unique prime factors of n
    primeFactors = [] # not unique
    m=n
    count=1
    while m >1:
        count+=1
        if m%count==0 and isPrime(count):
            primeFactors.append(count)
            m=int(m/count)
            count=1
    return primeFactors

def distinctFactors(n):
    # returns list of factors of n
    factors=[1]
    count=1
    for i in range(2,int(n/2)):
        if n%i==0:
            factors.append(int(i))
    factors.append(n)
    return factors

def findTriangleNumber():
    foundIt = False
    count=2000
    while not foundIt:
        print(count,end="\t")
        pascal3rdRow=count*(count+1)/2
        factors = distinctFactors(pascal3rdRow)
        print(len(factors),factors)
        if len(factors)>=500:
            return pascal3rdRow, distinctFactors(pascal3rdRow)
        if count>10000000000:#just in case
            return False
        count+=1

# main
n,factors=findTriangleNumber()
input("Triangle number",n,"has",len(factors),"factors")


