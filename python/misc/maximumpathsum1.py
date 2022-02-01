# maximum path sum 1

import numpy as np

triangle = [[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]



def copy2DList(theList):
    new = []
    row=[]
    for i in theList:
        row=[]
        for j in i:
            row.append(j)
        new.append(row)
    return new

def checkPath(path):
    # checks if path is valid
    for i in range(1,len(path)):
        diff=path[i]-path[i-1]
        if diff>1 or diff<-1:
            print("\n\nError there is a jump somewhere")
            return False
        elif path[i]>i:
            # here i wanna throw an index out of bounds exception...
            print("\n\nError index out of bounds")
            return False
    return True

def initSumTriangle(triangle):
    for i in range(len(triangle)-1,0,-1):
        # for each row starting from the bottom and ending at the third last
        for j in range(len(triangle[i])-1):
            # for each element of this excluding the last one 
            # (we sum the adjacent pairs and add this to the above thing)
            left = triangle[i][j]
            right = triangle[i][j+1]
            if left>=right:
                triangle[i-1][j]+=left
            else:
                triangle[i-1][j]+=right
    return triangle

def displayTriangle(triangle):
    for i in triangle:
        print(i)

def findPath(tri):
    # takes sumTriangle array and decides what the path should be
    path=[0]
    for i in range(1,len(tri)):
        left = tri[i][path[-1]]
        right = tri[i][path[-1]+1]
        if left>right:
            path.append(path[-1])
        else:
            path.append(path[-1]+1)
    return path

def heaviestPath(path,tri):
    # takes path and tri and returns the corresponding sum and then weights
    best=[]
    for i in range(len(tri)):
        best.append(tri[i][path[i]])
    return np.sum(best), best


# main

# this will be a triangle with each row gets the longest path added to it
sumTriangle = copy2DList(triangle)
sumTriangle = initSumTriangle(sumTriangle)

displayTriangle(sumTriangle) # the answer is the top one here 
displayTriangle(triangle)


# sequence of numbers which code for indices in path, it always starts with 0
path = findPath(sumTriangle)
if not checkPath(path):
    print("AAAAAAAAAAAHHHHHHHHHHH"*100)

# display the heaviest path
best = heaviestPath(path,triangle)
print("the best path is\n",path)
print("\nthis path gives\n",best)
#print("\nthe sum is", theSum)

