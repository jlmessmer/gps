import random
import copy
import collections
'''
Define a class for a Rock-Paper-Scissors graph
(A graph where each node has  n/2 out edges for n nodes and n/2 in edges)
'''
class Edge:
    def __init__(self, innode, outnode, weight = 0):
        self.innode = innode
        self.outnode = outnode
        self.weight = weight

    def __str__(self):
        return self.innode.name.zfill(4) + " --> " + self.outnode.name.zfill(4)

    def __repr__(self):
        return self.__str__()

class Node:
    def __init__(self, name, degree):
        self.name = name
        self.degree = degree
        self.outedges = []
        self.innodes = []
    def __str__(self):
        return self.name# + "\r\nNode Degree:\t" + str(self.degree)
    def __repr__(self):
        return self.__str__()

    def hasoutedge(self, node):
        for edge in self.outedges:
            if edge.outnode == node:
                return True
        return False
    
    def addoutedge(self, edge):
        if not(edge in self.outedges):
            self.outedges.append(edge)
    def addinnode(self, edge):
        if not(edge in self.innodes):
            self.innodes.append(edge)
    def indegree(self):
        return len(self.innodes)
    def outdegree(self):
        return len(self.outedges)
    def getinnodes(self):
        return self.innodes
    def iscomplete(self):
        if len(self.outedges) + len(self.innodes) == self.degree:
            return True
        return False
class Rgraph(object):    
    nodes = []
    outcompletenodes = []
    def gennodes(self, numnodes):
        for i in range(0, numnodes):
            self.nodes.append(Node(str(i), numnodes - 1))
#            print(self.nodes[i])

    def choosenextnode(self, startnode):
        next = random.randint(0, len(self.nodes) - 1)
        while next == startnode:
            next = random.randint(0, len(self.nodes) - 1)
        return next
    
    def genedges(self):
        nodequeue = collections.deque()
        nodestack = []
        degree = int(len(self.nodes) / 2)
        # Need to have n/2 out edges and n/2 in edges
        completednodes = []
        start = random.randint(0, len(self.nodes) - 1)
        node = self.nodes[start]

        possiblenodes = copy.copy(self.nodes)
        possiblenodes.remove(node)
        for i in range(0,degree):
            next = random.randint(0, len(possiblenodes) - 1)
            nextnode = possiblenodes[next]
            node.addoutedge(Edge(node, nextnode))
            nextnode.addinnode(node)
            possiblenodes.remove(nextnode)
        for n in possiblenodes:
            n.addoutedge(Edge(n, node))
            node.addinnode(n)
            nodequeue.append(n)
        completednodes.append(node)
        while nodequeue:            
            node = nodequeue.popleft()
            possiblenodes = copy.copy(self.nodes)
            possiblenodes.remove(node)
            for innode in node.getinnodes():
                if innode in possiblenodes:
                    possiblenodes.remove(innode)
            for cnode in  completednodes:
                if cnode in possiblenodes:
                    possiblenodes.remove(cnode)
            if node.outdegree() >= degree:
                for pnode in possiblenodes:
                    if pnode.outdegree() < degree:
                        pnode.addoutedge(Edge(pnode, node))
                        node.addinnode(pnode)
                        nodequeue.append(pnode)
                continue
            
            if len(possiblenodes) == 1:
                nextnode = possiblenodes[0]
                node.addoutedge(Edge(node, nextnode))
                nextnode.addinnode(node)
                completednodes.append(node)
                                
            elif len(possiblenodes) >= 1:
                outdeg = node.outdegree()
                for i in range(0, degree - outdeg):
                    next = random.randint(0, len(possiblenodes) - 1)
                    nextnode = possiblenodes[next]
                    node.addoutedge(Edge(node, nextnode))
                    nextnode.addinnode(node)
                    possiblenodes.remove(nextnode)

                    for pnode in possiblenodes:
                        if pnode.outdegree() < degree:
                            pnode.addoutedge(Edge(pnode, node))
                            node.addinnode(pnode)
                            nodequeue.append(pnode)                            
                completednodes.append(node)
        
    def resolve(self, m1, m2):
        # Return 0 if a tie
        # Return 1 if first move wins (player 1)
        # Return 2 if second move wins (player 2)
        if m1 == m2:
            return 0
        else:
            n1 = self.nodes[m1]
            n2 = self.nodes[m2]
            if n1.hasoutedge(n2):
                return 1
            else:
                return 2
    def print(self):
        print("==============================")
        for node in self.nodes:
            print("Node:\t" + str(node).zfill(4))
            print("\t" + str(node.outedges))
        print("==============================")
            
            
def main():
    size = input("How many moves do you want? ")
    size = int(size)
    rpsgraph = Rgraph()
    rpsgraph.gennodes(size)
    rpsgraph.genedges()
    rpsgraph.print()
if __name__ == "__main__" : main()
