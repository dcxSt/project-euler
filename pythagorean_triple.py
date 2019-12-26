###
# pythagorean triple problem project eiler, problem number 9
# PSEUDOCODE
# find the pythagorean tripple satisfying a+b+c =1000
## big nested for loop

###
import numpy as np

def main(n=1000):
    a,b=1,1
    while 2*a+np.sqrt(2*a**2) < 1000:
        while a+b + np.sqrt(a**2 + b**2) <= 1000:
            c = np.sqrt(a**2 + b**2)
            if int(c) == c:
                if a+b+c==1000:
                    return a*b*c
            b+=1
        a+=1
        b=a
    return False

print(main())
            
