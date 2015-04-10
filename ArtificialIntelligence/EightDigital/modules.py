#   coding = utf-8
#   Application Modules

import random

def randk(i,j):
    t = random.randint(i,j)
    return t

#   init matrix for eight digital
def range2rect(x,y,start=0,step=1):
    N=[]
    F=[]
    for i in range(x):                 
        for j in range(y):
            F.append(start)
            start += step
        N.append(F)
        F=[]
    return N
