#   coding=utf-8
#   Genetic Algorithms Sample
#   Language:   python
#   Author：    jiangfan
#   Tel:        13120394096
#   Data:       2015.4.6

from genetic_modules import *

class Node:
#        next = None
        data = None
        def __init__(self, data, result):
            self.data = data
            self.result = result         
        
#   init colony for four idiotypes
def init_gene():
    a = 0
    node = []
    node_temp = []
    while(a < 4):
        i = randk(0, 7)
        j = randk(0, 7)
        result = i*i + j*j
        m = dec2bin(i)
        n = dec2bin(j)
        data = add_bin(m,n)
        node.append(Node(data, result))
        node_temp.append(Node(data, result))
        a = a + 1
    return node


if __name__ == "__main__":
    a =0
    num = 0
    node = init_gene()

    while num < 5:
        node_temp = node
        fit = fitness(node)
        print(num, " colony:")
        while(a < 4):
            print(node[a].data)
    #        print(node[a].result)
    #        print(fit[a])
            a = a + 1
        print("select:")
        element = select(fit)
        a = 0
        while (a < 4):
            node[a].data = node_temp[element[a]].data 
            node[a].result = node_temp[element[a]].result 
            print(node[a].data)
            a += 1
        node = mate(node, node_temp)
        node = variation(node, node_temp)

        num += 1




  




















