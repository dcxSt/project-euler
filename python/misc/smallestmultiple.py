# 2520

def checkPrime(n): # returns boolean
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True

def primesSmallerThan(n): # returns all primes /leq n
    primes=[]
    for i in range(2,n+1):
        if checkPrime(i):
            primes.append(i)
    return primes

def mult(numbers): # returns all nums in list multiplied with each other
    # takes list of numbers and returns multiplyingall of them togethers
    n=1
    for i in numbers:
        n*=i
    return n

def primeFactors(n):
    # returns factors in list of the int n
    factors=[]
    i=2
    while n!=1:
        if n%i==0:
            n=n/i
            factors.append(i)
            i=1
        i+=1
    return factors

def main(biggest):
    primes=primesSmallerThan(biggest)
    factors=[] # this is a list of the prime factors that when multiplied
    # together - they compose the number we are looking for
    print("primes:",primes)
    for i in primes:
        m=i
        while m<=biggest:
            factors.append(i)
            m*=i
    number = mult(factors)
    print(factors)
    return number

# main 
# print(primeFactors(2520))
print(main(20))
