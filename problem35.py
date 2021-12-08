import numpy as np

def checkp(n):
    if n==2: return True
    for i in range(3,int(np.sqrt(n)+2),2):
        if n % i == 0: return False
    return True

count = 0
for n in range(2,10**2):
    if checkp(n):
        iscirc = True
        # b = [i for i in str(n)]
        # c = b.copy()
        # b.sort()
        # if c!=b:
        #     isgood = False
        for i in range(len(str(n))):
            if not checkp(int( str(n)[i:] + str(n)[:i] )):
                iscirc = False
        print(n)
        if iscirc:
            count += 1 

print(count)
