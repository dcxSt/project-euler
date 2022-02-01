import numpy as np

count = 0
n = 0 # number of digits checked
mult = 1
ns = [10**i for i in range(7)]
idx_curr_n = 0
while True:
    count += 1
    n += int(np.log10(count)+1)
#    if n == ns[idx_curr_n]:
#        mult *= int(str(count)[-1])
#        idx_curr_n += 1
#        if idx_curr_n == 7:
#            break
    if n >= ns[idx_curr_n]:
        dn = int(str(count)[ns[idx_curr_n] - n - 1])
        mult *= dn
        print("dn {}\nmult {}\nidx {}\n".format(dn,mult,idx_curr_n))
        idx_curr_n += 1
        if idx_curr_n == 7:
            break

print("\n\nRESULT")
print(mult)

