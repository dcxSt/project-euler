"""
digit cancelling fractions

pseudo: 

for each pair of one digit numbers
look at all multiples (where the smaller one is seen as the numerator)

for each two digit number if the numerator
for each two digit number in the denominator that is bigger than the numerator
check to see if the fraction is a non-trivial cancelling fraction
display the four fractions


"""

# takes numerator and denominator as 2-element tuples (array like i think) and returns boolean
curious = []
for a in range(1,9):
    for b in range(a+1,10):
        # a is the numerator and b is the denominator, b must be larger than a
        for i in range(2,int(100/b+2)):
            aprime,bprime = int(a*i),int(b*i)
            if len(str(aprime))!=2 or len(str(bprime))!=2:
                continue
            aprime,bprime = [int(str(aprime)[0]),int(str(aprime)[1])] , [int(str(bprime)[0]),int(str(bprime)[1])]
            
            if a in aprime and b in bprime:
                acopy,bcopy = aprime.copy(),bprime.copy()
                acopy.remove(a)
                bcopy.remove(b)
                if acopy[0]==bcopy[0] and acopy[0]!=0:
                   curious.append([a,b,aprime,bprime])

print('len curious',len(curious))
for i in curious:
    if i[2][1]==0 and i[3][1]==0:
        curious.remove(i)
        print('check')
    print(i)
    input()

for i in curious:
    print(i[0] ,"/", i[1],"\t=\t"+str(i[2][0])+''+str(i[2][1])+'/'+str(i[3][0])+''+str(i[3][1]))
    #print()

print('\n\n')
print('len curious',len(curious))

