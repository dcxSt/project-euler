import numpy as np
import decimal as dec
import continued_fractions as cf

dec.getcontext().prec = 128 # 128 decimal places precision

# it can be assumed that there are no solutions in positive integers when D is square
# x^2 - Dy^2 = 1

def y(x0:int , d:int):
    return np.sqrt((x0**2 - 1)/d)

def x(y0:int , d:int):
    return np.sqrt((d * y0**2 + 1))


"""
PSEUDOCODE

largest_x = 1

for each natural d below 1000
    generate the sequence of convergents
        check each convergent to see if it satisfies the equation, taking the numerator hi as x and the denominator ki as y
        if it solves the diophantine equation 
            check to see if x is the largest one yet found
                if it is, update the largest x
            break out of the convergents generating loop

"""

largest_x = 5
x_list = [] # list of x values
x_dic = {} # key = x, value = d
y_dic = {} # key = d, value = y

for d in range(2,1000):
    if np.sqrt(d) == int(np.sqrt(d)):
        continue 
    # generate the sequence of convergents
    sqrtd = np.sqrt(dec.Decimal("{:.0f}".format(d)))
    cfrac = cf.cfrac_seq(sqrtd , 100) # continued fraction sequence
    for i in range(1,len(cfrac) + 1):
        x , y = cf.get_hi_ki(cfrac[:i])
        # check to see if x and y solve the diophantine equation
        if x**2 - d * y**2 == 1:
            x_dic[x] = d
            y_dic[d] = y
            x_list.append(x)
            print("d={}\tx={}".format(d,x))
            largest_x = max(x , largest_x)
            break 


print("\nLARGEST X\nx = {}".format(largest_x))
print("\nLARGEST X'S D\nd = {}\n".format(x_dic[largest_x]))
print("\nLARGEST X'S Y\ny = {}\n".format(y_dic[x_dic[largest_x]]))

x_list.sort(reverse=True)
print(x_list[:5])

print("\n\nEnd")

