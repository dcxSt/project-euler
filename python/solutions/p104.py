import random
import sys

# approximately phi
phi = 1.61803398874989484820458683436563811772030917980576286213544862270526046281890244970720720418939113748475408807538689175212663386222353693179318006076672635443338908659593958290563832266131992829026788067520876689250171169620703222104

# the thousand'th fibonacci number
fib1000 = 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875

# first few hundred digits of the 10_000'th fibonacci number
fib10000 = 336447648764317832666216120051075433103021484606800639065647699746800814421666623681555955136337340255820653326808361593737347904838652682630408924630564318873545443695598274916066020998841839338646527313000888302692356736131351175792974378544137521305205043477016022647583189065278908551543661595829

def pandigital(n):
    s = str(n)
    if len(s) > 9: raise Error("wrong logic error")
    if len(s) != 9: return False
    for i in "123456789":
        if i not in s: return False
    return True

if __name__ == "__main__":
    n = 10000
    pbeg = fib10000
    pend1 = 238230626 # last 9 digits of 9999'th fibonacci number 
    pend2 = 947366875 # last 9 digits of 10000'th fibonacci number
    while True:

        ### iterate through to find next begining of the fib numbers
        n += 1
        pbeg *= phi
        pbeg = int(pbeg + 0.5)
        if len(str(pbeg)) > 250:
            pbeg = int(str(pbeg)[:250])

        ### iterate through, find last 9 digits of next fibonacci number
        pend1,pend2 = pend2,pend1+pend2
        pend1 %= 1000000000
        pend2 %= 1000000000

        # trace / log 
        if n % 100000 == 0:
            print("Trace")
            print("n={}\npbeg={}\npend={}".format(n,pbeg,pend2))
            print()

        if pandigital(str(pbeg)[:9]) and pandigital(pend2):
            print("\nGot it\n")
            print("n={}\npbeg={}\npend={}".format(n,pbeg,pend2))
            print()
            break





