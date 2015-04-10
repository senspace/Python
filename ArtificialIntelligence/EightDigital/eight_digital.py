#   coding=utf-8
#   Eignt Digital Sample
#   Language:   python
#   Author：    jiangfan
#   Tel:        13120394096
#   Data:       2015.4.6

#from modules import *   
import math    

def caclute_distance(n):
    T = [0, 1, 2]
    distance = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in T:
        for j in T:
            if n[i][j] == 1:
                distance[i][j] = i + math.fabs(j - 1)
            elif n[i][j] == 2:
                distance[i][j] = i + math.fabs(j - 2)
            elif n[i][j] == 3:
                distance[i][j] = math.fabs(i - 1) + j
            elif n[i][j] == 4:
                distance[i][j] = math.fabs(i - 1) + math.fabs(j - 1)
            elif n[i][j] == 5:
                distance[i][j] = math.fabs(i - 1) + math.fabs(j - 2)
            elif n[i][j] == 6:
                distance[i][j] = math.fabs(i - 2) + j
            elif n[i][j] == 7:
                distance[i][j] = math.fabs(i - 2) + math.fabs(j - 1)
            elif n[i][j] == 8:
                distance[i][j] = math.fabs(i - 2) + math.fabs(j - 2)
    total = 0
    for i in T:
        for j in T:
            total += distance[i][j]
    return int(total)

def init(m, n):
    T = [0, 1, 2]
    for i in T:
        for j in T:
            m[i][j] = n[i][j]

if __name__ == "__main__":
    a =0
    total = 0
    m = [[1, 4, 2], [3, 5, 0], [6, 7, 8]]
    n = [[1, 4, 2], [3, 5, 0], [6, 7, 8]]
    temp = [[1, 4, 2], [3, 5, 0], [6, 7, 8]]   
    a = 0
    while a<3:
        print(n[a])
        a += 1
    distance = caclute_distance(n)
    print("Distance", distance)

    print("First Moving: ")
    temp[1][2] = n[0][2]
    temp[0][2] = n[1][2]
    init(m, temp)
    distance = 1 + caclute_distance(m)
    print(distance)
    a = 0
    while a<3:
        print(m[a])
        a += 1
    init(temp, n)   
    temp[1][2] = n[1][1]
    temp[1][1] = n[1][2]
    distance_temp = 1 + caclute_distance(temp)
    print(distance_temp)
    if distance_temp < distance:
        init(m, temp)
        a = 0
        while a<3:
            print(m[a])
            a += 1
    init(temp, n)
    temp[1][2] = n[2][2]
    temp[2][2] = n[1][2]
    distance_temp = 1 + caclute_distance(temp)
    print(distance_temp)
    if distance_temp < distance:
        init(m, temp)
        a = 0
        while a<3:
            print(m[a])
            a += 1

    init(n, m)
    init(temp, m)
    print("Second Moving: ")
    temp[1][1] = n[0][1]
    temp[0][1] = n[1][1]
    init(m, temp)
    distance = 2 + caclute_distance(m)
    print(distance)
    a = 0
    while a<3:
        print(m[a])
        a += 1

    init(n, m)
    init(temp, m)
    print("Third Moving: ")
    temp[0][1] = n[0][0]
    temp[0][0] = n[0][1]
    init(m, temp)
    distance = 3 + caclute_distance(m)
    print(distance)
    a = 0
    while a<3:
        print(m[a])
        a += 1    

    print("success!")























