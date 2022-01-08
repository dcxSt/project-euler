# Pentagonal numbers

"""
for d = P_k - P_j to be minimized... hmmm, I guess 

generate a large list of pentagonal numbers
for each pair of pentagonal numbers check (o n^2) 

for each pentagonal number, add it to all in the list

"""
import numpy as np

p = lambda n: n*(3*n - 1) / 2
n_of_y = lambda y: (1 + np.sqrt(1 + 24*y)) / 6


def is_p(y:int):
    n = n_of_y(y)
    if n == int(n):
        return True
    return False 


upper = 10000
first_thousand = p(np.arange(1,upper,1))
mat_diff = np.array([first_thousand - p(n) for n in range(1,upper)])
mat_diff = abs(mat_diff)
mat_sum = np.array([first_thousand + p(n) for n in range(1,upper)])

diffs = []
diffs_dic = {}
for i in range(upper - 1):
    for j in range(i,upper - 1):
        if is_p(mat_diff[i,j]) and is_p(mat_sum[i,j]):
            diffs.append(mat_diff[i,j])
            diffs_dic[mat_diff[i,j]] = (i+1,j+1)
            print(i + 1,j + 1)

print(diffs_dic[min(diffs)],min(diffs))







