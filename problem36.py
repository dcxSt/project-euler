import numpy as np

def dectobin(n):
    k = int(np.log2(n)) + 2
    brep = ""
    for i in range(k):
        if (n // 2**i) % 2 == 1: brep = "1" + brep
        else: brep = "0" + brep

    # trim zeros off end
    while brep[0] == "0": # assume number is geq 1
        brep = brep[1:]

    return brep

def ispalen(n: str):
    # assume n is a string
    if n == n[::-1]: return True
    return False

s = 0
for i in range(1,10**6):
    if ispalen(str(i)):
        if ispalen(dectobin(i)):
            s += i

print("s = {}".format(s))
