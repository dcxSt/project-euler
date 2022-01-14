import pandas as pd
import numpy as np

def sign(n):
    if n > 0: return True
    return False



df = pd.read_csv("p102_triangles.txt",delimiter=",",names=["0","1","2","3","4","5"])


:tabe a


counter = 0

for index,row in df.iterrows():
    x = np.array([row[0],row[1]])
    y = np.array([row[2],row[3]])
    z = np.array([row[4],row[5]])

    origin = np.array([0,0]) 
    origin_inside = True
    for i,j,k in [[x,y,z],[y,z,x],[z,x,y]]:
        perp = j - k
        perp = np.array([perp[1] , -perp[0]])
        ij = j - i
        oj = j - origin
        if sign(np.dot(ij , perp)) != sign(np.dot(oj , perp)):
            origin_inside = False

    if origin_inside:
        counter += 1

print(counter)

counter
counter
counter
counter
counter
counter
counter



Vim
