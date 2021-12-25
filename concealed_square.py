

def check(n):
    if len(str(n)) != 19:
        if len(str(n)) < 19:
            print("too small")
        else:
            print("too big")
        return False
    ns = str(n)
    if ns[0]=="1" and ns[2]=="2" and ns[4]=="3":
        print(ns)
        if ns[6]=="4" and ns[8]=="5" and ns[10]=="6":
            if ns[12]=="7" and ns[14]=="8" and ns[16]=="9" and ns[18]=="0":
                print("Fount it:")
                print(ns)
                return True

count = 10**9
while True:
    count+=10 # because it's definitely divisible by two and five
    sq = count**2
    if sq % 10001 == 0: print(sq)
    bl = check(sq)
    if bl:
        break
