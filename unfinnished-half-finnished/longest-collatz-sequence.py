# longest collatz sequence

import numpy as np
import time

longest = 1
longestLen = 1
#start = 2
check=0
cutoff=[[200,125]]

"""I ran this program a couple times and deduced that if at one point the sequence is at a number under 101 then 
My aim is to find the highest collatz seqsuence for now reallllllly big starting numbers so i have to make
my algorithem a little more efficient"""

def discount(count,longestLen,n):
    # method that takes cound and the longestLen and n, the current number that we're at 
    # and discounts it if it is known that this cannot outgrow the longest, returns boolean
    # idea, whenever you find a new maxima, add it to a list so that everything under that gets checked
    toGo=longestLen-count
    """if n<=200 and toGo >125:
        #print("a",end="")
        return True
    if n<=1000 and toGo > 179:
        #print("b",end="")
        return True
    if n<=10000 and toGo > 262:
        #print("c",end="")
        return True
    if n<=100000 and toGo > 351:
        #print("d",end="")
        return True
    if n<=1000000 and toGo > 525:
        #print("e",end="")
        return True
    if n<=10000000 and toGo > 686:
        return True"""
    #cutoff=[[200,125],[1000,179],[10000,262], [100000,351],[1000000,525],[10000000,686]]
    for i in cutoff:
        # this is same as above, now delete the above and generate the cutoff list automatically and cleverly (with new maxima)
        if n<=i[0] and toGo > i[1]:
            return True
    
    return False

def saveCutoff(name):
    # saves cutoff list to txt file so that we can reuse
    if name[-4:]!=".txt":
        print("error the name you typed is invalid")
        return False
    textFile=open(name,"w")
    for i in cutoff:
        textFile.write(str(i[0]))
        textFile.write("\n")
        textFile.write(str(i[1]))
        textFile.write("\n")
    textFile.close()
    print(name,"sucessfully saved")

def loadCutoff(name):
    # loads cutoff
    # stores cutoff temporarily in local variable
    tempCutoff=[]
    try:
        textFile = open(name,"r")
        print("checkcheckcheckcchkkkkkeeee1")
        line1=textFile.readline()
        print("checkcheckcheckcchkkkkkeeee1.5")
        line2=textFile.readline()
        print("checkcheckcheckcchkkkkkeeee2")
        while line2:
            tempCutoff.append([int(line1),int(line2)])
            print(tempCutoff)
            line1=textFile.readline()
            line2=textFile.readline()
            
        textFile.close()
        return tempCutoff
            

    except:
        print("IOError angry face")
        return False


# main
start_time = time.time()
# optional load a cutoff file
cutoff=loadCutoff("cutoff2.txt")
if not cutoff:
    print("\nErrororororororor\n"*25)

# generate a bunch of collatz sequences to see which one will give you the longest, this is the main loop
for start in range(200,1000001):
    # just to display for the user
    check+=1
    if check%100000==0:
        print("Check: ",check)
    # just to display for the user

    n = start
    count=1
    while n !=1:
        # this if statement is a safety net but may be slowing down the program
        """
        if n<1:
            print("Error")
            break"""
        
        count+=1
        # this is how the collatz sequence is defined
        if n%2==0:
            n = int(n/2)
        else:
            n = int(3*n+1)
        # every x counts check to see if we can disqualify it from the biggest number race
        x=8
        if count%x==0:
            if discount(count,longestLen,n):
                #print("!",end="")
                break
    if count > longestLen:
        # first we modify the cutoff list, unless you want the program to run faster in which case just load one and comment this out
        
        if cutoff[-1][0]*2*np.power(0.98,len(cutoff)+1) < start:
            cutoff.append([start-1,longestLen])
            print(start,"\t",count)
        longestLen = count
        longest = start

print("--- %s seconds ---" % (time.time() - start_time))
#saveCutoff("cutoffLogLong-0.98.txt")
print("\nThe longest sequence starts at: ",longest)
print("\nThe length of this sequence is\n",longestLen)
print("\n",cutoff,"\n")

n=longest
print("\n\n",n)
while n!=1:
    if n%2==0:
        n=int(n/2)
    else:
        n=int(3*n+1)
    print(n,end=", ")

