# problem 153 investigating gaussian integer

# import statements
import sys
import numpy as np
from datetime import datetime

start_time = datetime.now()

def primes(n):
    if n < 2: return
    yield 2
    plist = [2]
    for i in range(3,n):
        test = True
        for j in plist:
            if j>n**0.5:
                break
            if i%j==0:
                test=False
                break
        if test:
            plist.append(i)
            yield i

# returns prime factors bigger than 1 and smaller than n
def pfactors(n):
    for p in primes(n):
        while n%p==0:
            yield p
            n=n//p
            if n==1: return

# this one is useless, will keep until sure
def pfactors_with_n(n):
    yield n
    for p in primes(n):
        while n%p==0:
            yield p
            n=n//p
            if n==1: return

# returns all the factors of n including 1 and it's self
def factors(n):
    for p in range(1,n+1):
        if n%p==0:
            yield p

# very long, but does same as below (with same result)
def sum_of_all_factors_2(n):
    # 8224740835
    the_sum = 0
    for i in range(1,n+1):
        if i%1000==0:
            print(i)
        the_sum += sum(factors(i))
    return the_sum

# sums all factors of all numbers /leq n
def sum_int_factors(n):
    # 8224740835
    the_sum = n-1 # otherwise 1 is counted twice # summing all ones
    the_sum += int(n*(n+1)/2) # summing all ns
    for i in range(2,1+int(np.sqrt(n+1))):
        j = i
        the_sum += i
        j+=1
        while j * i <= n:
            the_sum += i+j
            j += 1
    return the_sum

# to calculate the sum of all real parts of positive parts of gaussian factors - overestimates
def find_gaussian_factors_sum(n,the_sum):
    factors_of = [[] for i in range(n+1)]#trace, has extra like that index is number
    for a in range(1,int(np.sqrt(n))+10):
        if a%100==0:
            print("a :",a)
        b=1
        while b<=a:
            if len(set(pfactors(a)).intersection(pfactors(b))) == 0:# if relatively prime
                alpha = 1
                while (a**2 + b**2) * alpha**2 <= n:
                    beta = alpha
                    while alpha * beta * (a**2 + b**2) <= n:
                        number = alpha * beta * (a**2 + b**2)#trace
                        if a==b and alpha!=beta:
                            the_sum += 2*(alpha*a + beta*a)
                            factors_of[number].append([a*alpha,a*alpha])#trace
                            factors_of[number].append([a*alpha,-a*alpha])#trace
                            factors_of[number].append([a*beta,a*beta])#trace
                            factors_of[number].append([a*beta,-a*beta])#trace
                        elif a==b and alpha==beta:
                            the_sum += 2*alpha*a
                            factors_of[number].append([a*alpha,a*alpha])#trace
                            factors_of[number].append([a*alpha,-a*alpha])#trace
                        elif a!=b and alpha==beta:
                            the_sum += 2*alpha*(a+b)
                            factors_of[number].append([a*alpha,b*alpha])#trace
                            factors_of[number].append([a*alpha,-b*alpha])#trace
                            factors_of[number].append([b*alpha,a*alpha])#trace
                            factors_of[number].append([b*alpha,-a*alpha])#trace
                            
                        else:
                            the_sum += 2*(alpha + beta)*(a + b)
                            factors_of[number].append([a*alpha,b*alpha])#trace
                            factors_of[number].append([a*alpha,-b*alpha])#trace
                            factors_of[number].append([a*beta,b*beta])#trace
                            factors_of[number].append([a*beta,-b*beta])#trace
                            factors_of[number].append([b*alpha,a*alpha])#trace
                            factors_of[number].append([b*alpha,-a*alpha])#trace
                            factors_of[number].append([b*beta,a*beta])#trace
                            factors_of[number].append([b*beta,-a*beta])#trace
                        beta+=1
                    alpha+=1
            b+=1
    return the_sum,factors_of

# main method
def main(n=int(10**5)):

    the_sum = sum_int_factors(n)
    print("sum of all factors:",the_sum)

    the_sum = find_gaussian_factors_sum(n,the_sum)

    end_time = datetime.now()

    print("\n\nBehold the sum:",the_sum)
    print("\nYour program took ",(end_time - start_time)," time to run")
    input("\n\nEnter to exit")


# method that is precise but slow
# returns 1 - list where each entry is the list of positive real gaussian factors of index
#         2 - list where each entry is the sum of the real parts
#         3 - the overall sum of 2
def gaussian_factors(n):
    factors_of = [[] for i in range(n+1)]
    the_sum=0
    for i in range(1,n+1):
        facs_of_i = g_factor(i)
        factors_of[i]=facs_of_i
        the_sum += sum([j[0] for j in factors_of[i]])
    print("the sum:",the_sum)
    return the_sum,factors_of


# helper for gaussian_factors:
# returns list of positive real part gaussian factors of n
def g_factor(n):
    gaussian_factors = [[1,0]]
    for a in range(1,int(np.sqrt(n))+10):
        for b in range(0,int(np.sqrt(n))+10):
            if [a,b] not in gaussian_factors:
                # if a+ib divides n, add a+ib to the list as well as what n/a+ib = 
                c = int(a**2+b**2)
                if int(n*a)%c == 0 and int(n*b)%c==0:
                    gaussian_factors.append([a,b])
                    gaussian_factors.append([a,-b])
                    if a!=b and b!=0:
                        gaussian_factors.append([b,a])
                        gaussian_factors.append([b,-a])
                    x = int(n*a/c)
                    y = int(-n*b/c)
                    
                    gaussian_factors.append([x,y])
                    gaussian_factors.append([x,-y])
                    if x!=y and y!=0:
                        gaussian_factors.append([y,x])
                        gaussian_factors.append([y,-x])
    if n!=1:
        gaussian_factors.append([n,0])
    # get rid of remaining duplicates
    gaussian_factors = [gaussian_factors[i] for i in range(len(gaussian_factors)) if gaussian_factors[i] not in gaussian_factors[:i]]
    return gaussian_factors

# helper method for the above
def display_g_factors(gaussian_factors):
    for i in gaussian_factors:
        if i[1]!=0:
            if i[1]>0:
                print(str(i[0])+" + "+str(i[1])+"i",end=" , ")
            else:
                print(str(i[0])+" - "+str(-i[1])+"i",end=" , ")
        else:
            print(str(i[0]),end=" , ")

def check_duplicates(facs):
    tupfacs = [tuple(i) for i in facs]
    no_dup = [tupfacs[i] for i in range(len(facs)) if facs[i] not in facs[:i]]
    if len(set(tupfacs).difference(set(no_dup))) >0:
        print("here found some duplicates")
        return True
    return False
    
"""
print("\n")
display_g_factors(g_factor(5))
print("\n")

n=5
the_sum1,the_factors1 = gaussian_factors(n)
"""
n=100000
the_sum2 = sum_int_factors(n)
the_sum2,the_factors2 = find_gaussian_factors_sum(n,the_sum2)

#print("1 :",the_sum1,"\t2 :",the_sum2)

#print("\n\n")

for i in range(len(the_factors2)):
    if i % 1000==0:
        print(i,end=" ")
    if check_duplicates(the_factors2[i]):
        print(i,"has duplicates")

print("press enter to exit:")
input()