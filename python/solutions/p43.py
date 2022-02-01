import numpy as np

primes = [2,3,5,7,11,13,17]

def check_pandigital(n):
    if len(str(n)) != 10:
        return False 
    for i in str(n):
        if i not in "0123456789":
            return False
    return True

def check_property(n):
    # returns True if n is a 10 digit number pandigital from 0 through 9
    for i in range(7):
        k = int(str(n)[i+1:i+4])
        if k % primes[i] != 0:
            return False
    return True

def generate_combinations(digits,ds="1234567890"):
    if digits == "":
        for d in "123456789":
            all_ds = "1234567890"
            idx = all_ds.index(d)
            all_ds = all_ds[:idx] + all_ds[idx+1:]
            for n in generate_combinations(d,all_ds):
                yield n
    elif len(ds) == 1:
        yield digits + ds
    else:
        for d in ds:
            remaining_ds = ds
            new_digits = digits + d
            idx = remaining_ds.index(d)
            remaining_ds = remaining_ds[:idx] + remaining_ds[idx+1:]
            for n in generate_combinations(new_digits , remaining_ds):
                yield n

s = 0 # the sum that will be the solution to the problem

for n in generate_combinations("", "1234567890"):
    print(n)
    n = int(n)
    if check_pandigital(n):
        if check_property(n):
            s += n

print(s)


