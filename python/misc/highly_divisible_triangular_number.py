# project euler problem 12
from functools import reduce

def factors(n):
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0)))

def nfact(n):
    return len(factors(n))

def factors_smaller_than_sqrt(n):
    return set(reduce(list.__add__,([i] for i in range(1, int(n**0.5)+1) if n%i == 0)))

if __name__ == "__main__":
    print(factors(100))
    print(factors_smaller_than_sqrt(100))
    print("number of factors of 100")
    print(nfact(100))

    count, nt = 0, 0
    while True:
        if count % 10000 == 0: print("\ncount:{}\nnt:{}".format(count, nt))
        count +=1
        nt += count
        n_of_factors = nfact(nt)
        if n_of_factors >= 500:
            print("\n\nFount it\ncount: {}\nnt: {}".format(count, nt))
            print("Number of factors: {}".format(n_of_factors))
            input("[Enter to exit]")
            break 


