import numpy as np



f = open("large_numbers.csv","r")
lines = f.readlines()
numbers_string = [l[:-3] for l in lines]
numbers = [int(l[:-3]) for l in lines]

numbers_array = [[int(d) for d in l[:-3]] for l in lines]
nmat = np.array(numbers_array)

decimals = 50
first_fifteen_digets = np.array([0 for i in range(15)])

for idx,col in enumerate(nmat.T):
    the_sum = sum(col)
    first_fifteen_digets[idx] += int(the_sum // 1000)
    the_sum -= int(the_sum // 1000) * 1000
    first_fifteen_digets[idx + 1] +=  the_sum // 100
    the_sum -= int(the_sum // 100) * 100
    first_fifteen_digets[idx + 2] += the_sum // 10 
    the_sum -= int(the_sum // 10) * 10
    first_fifteen_digets[idx + 3] += the_sum
    print()
    for i in first_fifteen_digets:
        print(i, end=" ")


