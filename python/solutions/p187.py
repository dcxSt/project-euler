
import numpy as np
from CheckPrime import checkPrime

num = 3# start at 1 from 2*2 and 3*3 and 3*2

#for a in range(2,10**4):
 #   if checkPrime(a):
  #      for b in range(a,10**8):
   #         if a*b>10**8:
    #            break                
     #       if checkPrime(b):
      #          num+=1

#print(num)

n = input('test number here')
if not n: n=10**8
else: n=int(n)
sqrtn = int(np.sqrt(n))

for b in range(6,n,6):
    print(b)
    if 2*(b-1)>n:
        break
    elif checkPrime(b-1):
        num+=1
    if 2*(b+1)>n:
        break
    elif checkPrime(b+1):
        num+=1

for b in range(6,n,6):
    if 3*(b-1)>n:
        break
    elif checkPrime(b-1):
        num+=1
    if 2*(b+1)>n:
        break
    elif checkPrime(b+1):
        num+=1

for a  in range(6,sqrtn,6):
    if a%6**5==0: print(a)#trace
    if checkPrime(a-1):
        num+=1
        for b in range(a+6,n,6):
            if (a-1)*(b-1)>n:
                break
            elif checkPrime(b-1):
                num+=1
            if (a-1)*(b+1)>n:
                break
            elif checkPrime(b+1):
                num+=1
    if checkPrime(a+1):
        num+=1
        if checkPrime(a-1): num+=1
        for b in range(a+6,n,6):
            if (a+1)*(b-1)>n:
                break
            elif checkPrime(b-1):
                num+=1
            if (a+1)*(b+1)>n:
                break


print('\n\nnumber is : ',n)

