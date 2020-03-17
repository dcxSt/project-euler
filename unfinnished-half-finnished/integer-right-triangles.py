# integer right triangles
import numpy as np

def checkSquare(n): # returns boolean : True if n has a natural root
    if np.square(int(np.sqrt(n)))==n:
        return True
    return False

def isInteger(n): # returns boolean
    if n-int(n)==0:
        return True
    return False

def checkPrime(n): # returns boolean
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True

def pairFactors(ab):
    pairFactor=[]
    if checkPrime(ab):
        return [(1,ab)]
    # go through numbers smaller than it see if they divide
    for i in range(1,int(np.sqrt(ab)+1)):
        if ab%i==0 and (int(ab/i),i) not in pairFactor:
            pairFactor.append((i,int(ab/i)))
    return pairFactor

def rightTriangles(p,scilent=False): # takes perimiter and returns array of all the lengths of the sides of all possible right triangles with that perimiter
    triangles=[]
    # c >= a,b and c <= a+b, this narrows our search, with a^2+b^2=c^2
    # i did some maths and:
    # p = c +- sqrt(2ab-c^2) => (p-c)^2+c^2 = 2ab
    for c in range(int(p/3),int(p/2)):
        ab = (np.square(p-c)-np.square(c))/2
        if isInteger(ab):
            ab=int(ab)
            pairFactor=pairFactors(ab)
            for i in pairFactor:
                a = i[0]
                b = i[1]
                if a+b+c==p:
                    triangles.append([a,b,c])
    if not scilent:
        if len(triangles)>=10: # can change this value if you want, it's for show
            print("perimeter ",p,"has triangles",len(triangles),":\n",triangles)
    return triangles


def main():
    perimeters=[0]
    biggest=0
    for p in range(1,1001):
        triangles=rightTriangles(p)
        if len(triangles) >= biggest:
            if len(triangles)==biggest:
                perimeters.append(p)
            else:
                perimeters=[p]
                biggest=len(triangles)
    return perimeters,biggest


perimeters,biggest = main()
p = np.sum(perimeters)
tri = rightTriangles(p,scilent=True)
print("\nPerimeter of length",p)
print("has the following", len(tri),
"right angled triangles associated with it")
print(tri)
input("\n\npress enter to exeunt")




