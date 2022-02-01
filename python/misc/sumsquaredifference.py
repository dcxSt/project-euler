# sum square difference

import numpy as np

def squareOfSum(n):
    theSum=0
    for i in range(1,n+1):
        theSum+=i
    return np.square(theSum)

def sumOfSquares(n):
    theSum=0
    for i in range(1,n+1):
        theSum+=np.square(i)
    return theSum

print(squareOfSum(100)-sumOfSquares(100))
