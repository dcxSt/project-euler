# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
# 
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
# 

from nth_prime import get_nth_prime, is_prime

def get_next_prime(p):
    # get the smallest prime that is bigger than p, p is assumed to be odd
    k = p
    while True:
        k += 2
        if is_prime(k):
            return k

def check_property(primes=[2,3,5,7,11]):
    # first do a quick test to see if any concats are divisible by three
    # for this to be the case all the numbers must be equal mod three, except for three it's self
    if primes[1] % 3 != primes[2] % 3 or primes[3] % 3 != primes[4] % 3 or primes[1] % 3 != primes[3] % 3: return False
    # now we know that all are same mod three
    if primes[0] != 3 and primes[0] % 3 != primes[1] % 3: return False
    for i in primes:
        for j in primes:
            if i != j:
                if not is_prime(int(str(i) + str(j))):
                    return False
    return True 

n = 5
# nth_primes = [1,2,4,29,155,100000] # the last digit in this list acts as an upper limit, the program will crash if it is ever attained
# primes = [2,3,7,109,907]

nth_primes = [2,3,4,29,30,10000]
primes = [3,5,7,109,get_nth_prime(30)]

# nth_primes = [2,3,29,122,10000]
# primes = [3,5,109,673]

count = 0 
while True:
    # pseudocode
    # 
    # start on the left, if the index is only one smaller than the index directly on his right, reset this to a small prime value and move to the next index
    # if there is a difference bigger than 1, increment this prime to the next prime and add one to the nth_primes list which 
    count += 1
    incidx = 0 # the index of the prime you (out of 5) you want to increment
    while nth_primes[incidx+1] - nth_primes[incidx] == 1:
        nth_primes[incidx] = incidx + 1
        # primes[incidx] = get_next_prime( primes[incidx] )
        primes[incidx] = get_nth_prime(incidx + 2) # slow
        incidx += 1
    nth_primes[incidx] += 1
    primes[incidx] = get_next_prime( primes[incidx] )
    if count % 1000000 == 0:
        print(primes)
    if check_property(primes):
        print("\nFount it")
        print(primes)
        print("the sum is", sum(primes))
        with open("problem60_result.txt","w+") as f:
            f.write("Fount it\n")
            f.write(str(primes))
            f.write("\nthe sum is "+ str(sum(primes)) )
            f.write("\n")
        input("\n\n[Enter to continue]")
        print("\n\nContinuing search\n")
    


