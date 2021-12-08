
single_diget = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
second_diget = {2:6, 3:6, 4:6, 5:5, 6:5, 7:7, 8:6, 9:6}
teens = {10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}

def n_to_word_len(n):
    wl = 0
    if n>=100 and n<1000:
        wl += single_diget[int(str(n)[0])] # for single diget one in one hundred
        wl += 3 # and
        wl += 7 # hundred
        try:n = int(str(n[1:]))
        except:
            try: n = int(str(n)[2:])
            except:
                return wl
    elif n == 1000:
        return 3 + 8

    # now only two digets
    if n >= 20:
        wl += second_diget[int(str(n)[0])]
        n = int(str(n)[1:])
        if n == 0: 
            return wl
    if n < 10 and n!=0:
        wl += single_diget[n]
    elif n==0:
        pass
    else: # n >= 10 and n < 20
        wl += teens[n]
    return wl


total = 0
for i in range(1,1001):
    total += n_to_word_len(i)
    print(i, ":", n_to_word_len(i))
print(total)
