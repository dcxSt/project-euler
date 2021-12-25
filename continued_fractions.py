import numpy as np
import decimal as dec

dec.getcontext().prec = 128

# this program finds the continued fraction sequence to the square root of n

def gcd(a:int,b:int):
    # takes two ints, returns their greatest common divisor
    if a > b:
        r = a % b
        if r == 0:
            return b
        return gcd(b,r)
    elif a < b:
        r = b % a
        if r == 0:
            return a
        return gcd(a,r)
    return a # this is when a = b 

def cfrac_seq(sqrtn,length):
    r = sqrtn - int(sqrtn) 
    cfrac = [int(sqrtn)]
    for i in range(length):
        a = int(1/r)
        cfrac.append(a)
        r = 1/r - a
    return cfrac

def get_hi_ki(cfrac):
    # takes a continued fraction sequence and obtains the numerator hi and denominator ki
    cf = cfrac.copy() # [i for i in cfrac]
    hi , ki = 1 , cf[-1]
    cf = cf[:-1]
    for a in cf[::-1]:
        hi , ki = ki , hi + a * ki
    hi,ki = ki,hi # flip them once
    g = gcd(hi,ki)
    return hi//g , ki//g # the // operator is there just to keep them as ints

def eval_frac_seq(cfrac):
    cf = [dec.Decimal(i) for i in cfrac]
    est = cf[0]
    cf = cf[1:]
    
    def frac_gen(cf):
        if len(cf) > 1:
            return 1 / (cf[0] + frac_gen(cf[1:]))
        else:
            return 1 / cf[0]

    est += frac_gen(cf)
    return est


if __name__ == "__main__":
    phi = 1.61803398875 
    print("golden ratio phi continued fraction is = {}".format(cfrac_seq(phi , 100)))
    two = dec.Decimal(2.)
    sqrt2 = np.sqrt(two)
    print("sqrt of 2 continued fraction is = {}".format(cfrac_seq(sqrt2 , 100)))
    
    
    print("\n")
    print("Evaluating the continued fractions")
    print("phi\n{}\n{}".format(phi , eval_frac_seq(cfrac_seq(phi,10))))
    print("sqrt 2\n{}\n{}".format(np.sqrt(2) , eval_frac_seq(cfrac_seq(sqrt2,60))))
    
    
    print("\n")
    print("Evaluating numerator and denominator of the fractions")
    hi,ki = get_hi_ki([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    print("phi = {}\nhi = {}\nki = {}\nquotient = {}\n".format(phi , hi , ki , hi/ki))
    hi,ki = get_hi_ki([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
    print("sqrt 2 = {}\nhi = {}\nki = {}\nquotient = {}\n".format(np.sqrt(2) , hi , ki , hi/ki))
    






