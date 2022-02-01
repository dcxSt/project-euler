import numpy as np

# it can be assumed that there are no solutions in positive integers when D is square
# x^2 - Dy^2 = 1

def y(x0,d):
    return np.sqrt((x0**2 - 1)/d)

def x(y0,d):
    return np.sqrt((d * y0**2 + 1))

largest_x = 5

#for d in range(2,1000):
#    if np.sqrt(d) != int(np.sqrt(d)):
#        # lagrange proved that so long as D is not a perfect square, Pell's equation has infinitely many distinct integer solutions 
#        x = 2
#        while y(x,d) != int(y(x,d)):
#            x += 1
#        if x > largest_x and x < 10**7:
#            largest_x = x
#            print("d={} : x={}\t{}^2 - {} * {}^2 = 1".format(d,x,x,d,int(y(x,d))))
#        

# I should actually look throught the ys
for d in range(2,1000):
    if np.sqrt(d) != int(np.sqrt(d)):
        y0 = 1
        x0 = x(y0,d)
        while x0 != int(x0):
            y0 += 1
            x0 = x(y0,d)
        if x0 > largest_x:
            largest_x = int(x0)
            print("d={} : x={}\t{}^2 - {} * {}^2 = 1".format(d,x0,x0,d,int(y(x0,d))))


print("\n\nËnd")

