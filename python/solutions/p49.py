import numpy as np

def isprime(n):
    if n == 1: return False
    if n == 2: return True
    if n == 3: return True
    else:
        if n%2 == 0: return False
        for k in range(3 , int(np.sqrt(n) + 1) , 2):
            if n % k == 0: return False
        return True

def rmchar(word, c):
    idx = word.index(c)
    return word[:idx] + word[idx+1:]

def isperm(a,b,c):
    ast, bst, cst = str(a), str(b), str(c)
    for ch in ast:
        if ch in bst and ch in cst:
            bst = rmchar(bst, ch)
            cst = rmchar(cst, ch) 
        else: return False
    return True


for n in range(1001 , 10000 , 2):
    if isprime(n):
        for step in range(2,((10000 - n) // 2) , 2):
            if isperm(n , n+step,n+2*step) and isprime(n+step) and isprime(n+2*step):
                pass
                print("{} + {} + {}".format(n, n+step,n+2*step))


