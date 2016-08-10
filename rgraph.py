import random
'''
Define a class for a Rock-Paper-Scissors graph
(A graph where each node has  n/2 out edges for n nodes and n/2 in edges)
'''
class Edge:
    def __init__(self, innode, outnode, weight = 0):
        self.innode = innode
        self.outnode = outnode
        self.weight = weight

class Node:
    outedges = []
    inedges = []
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()
    def addoutedge(self, node):
        if !(node in outedges):
            outedges.append(node)
    def addinedge(self, node):
        if !(node in inedges):
            inedges.append(node)
class Rgraph(object):    
    nodes = []
    def gennodes(self, numnodes):
        for i in range(0, numnodes):
            self.nodes.append(Node(str(i)))
            print(self.nodes[i])
    def genedges(self):
        # Need to have n/2 out edges and n/2 in edges
        completednodes = []
        startnode = random.randint(0, len(self.nodes) - 1)
        while len(completednodes) != len(nodes):
            node = self.nodes[startnode]
            
def main():
    rpsgraph = Rgraph()
    rpsgraph.gennodes(5)
if __name__ == "__main__" : main()
