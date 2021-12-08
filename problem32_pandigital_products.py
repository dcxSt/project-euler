import numpy as np

def check_mulpan(a,b):
    """ checks if the product of a and b together with a and be are pandigital
    returns bool """
    str_rep = str(a) + str(b) + str(a*b)
    if len(str_rep) != 9 or "0" in str_rep:
        return False
    for i in "123456789":
        if i not in str_rep:
            return False
    return True

thesum = 0
products = []
for a in range(2,10000): # upper bound five zeros not inclusive
    for b in range(1,a):
        if check_mulpan(a,b) and a*b not in products:
            thesum += a*b
            products.append(a*b)
            print("Found one!\t{} * {} = {}".format(a,b,a*b))
            print()

print("The sum is")
print(thesum)
        
