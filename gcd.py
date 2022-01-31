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

