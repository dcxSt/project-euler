# largest palindrome product

"""
gonna do this by math instead of brute force,
so first i will generate a bunch of pallindromes
"""

# checks if palindrome
def checkPalindrome(n):#n is int
    #print("n=",n)
    n = str(n)
    m=""
    for i in range(len(n)-1,-1,-1):
        #print(i)
        m+=n[i]
    n=int(n)
    m=int(m)
    #print("\n",n,m)
    if n==m:
        return True
    return False

biggest=0
palindromes=[]
# a, b, c
for n in range(100,1000):
    for i in range(99,n):
        p=i*n
        if checkPalindrome(p):
            palindromes.append([i,n,p])
            if p>biggest:
                biggest=p

print("\nbiggest palindrome",biggest)
print("\npalindromes",palindromes)
print("\nbiggest palindrome",biggest)

import matplotlib.pyplot as plt
import numpy as np

palindromes = np.transpose(palindromes)
plt.figure()
plt.plot(palindromes[2])



