# this is wrong, i did a easy thing instead.
import numpy as np

def isprime(x):
    # assume x is natural number
    if x==2:return True
    elif x==3:return True
    elif x==1:return False
    else:
        for n in range(3,int(np.sqrt(x) + 2),2):
            if x%n==0:return True
    return False

def is_square(x):
    if np.sqrt(x) == int(np.sqrt(x)): return True
    return False

def is_cubed(x):
    if x**(1./3.) == int(x**(1./3.)): return True
    return False

def is_fifth_root(x):
    if x**(1./5.) == int(x**(1./5.)): return True
    return False

s = 0 # sum
for a in range(2,101):
    print("a={}".format(a),end="\t")
    if is_square(a):
        # only count those after the square root to the power of 100, a^51 is the first unique one
        print("square {}".format(a))
        s += 50
    elif is_cubed(a):
        # only count those after the cube root to the power of 100, a^34 is the first unique one
        print("cube {}".format(a))
        s += 67 # 100 - 33
    elif is_fifth_root(a):
        print("fifth power {}".format(a))
        # a^21 is the first unique one
        s += 80 # 100 - 20
    else:
        s += 99
    print("sum is",s)

print("\n=================================\nsum = {}".format(s))
