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
        return self.innode.name + " --> " + self.outnode.name

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
    def addoutedge(self, edge):
        if not(edge in self.outedges):
            self.outedges.append(edge)
    def addinnode(self, edge):
        if not(edge in self.innodes):
            self.innodes.append(edge)
    def indegree(self):
        return len(self.innodes)
    def getinnodes(self):
        return self.innodes
    def iscomplete(self):
        if len(self.outedges) + len(self.innodes) == self.degree:
            return True
        return False
class Rgraph(object):    
    nodes = []
    nodequeue = collections.deque()
    nodestack = []
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
#        nodequeue = collections.deque()
        nodestack = []
        # Need to have n/2 out edges and n/2 in edges
        completednodes = []
        startnode = random.randint(0, len(self.nodes) - 1)

        node = self.nodes[startnode]
        self.nodestack.append(node)
#        self.nodequeue.append(node)
        while self.nodestack:
            node = self.nodestack.pop()
            if node in self.outcompletenodes and len(node.innodes) >= 2:
                continue
            possiblenodes = copy.copy(self.nodes)
            possiblenodes.remove(node)
#            print(node)
#            print(str(self.outcompletenodes))
            self.outcompletenodes.append(node)
            self.processnode(node, possiblenodes)
        
        #print(node)

    def processnode(self, node, possiblenodes):
        for pnode in possiblenodes:
            if pnode in node.getinnodes() or pnode.indegree() >= 2:
                possiblenodes.remove(pnode)                
        print(node.name + ":\t" + str(possiblenodes) + "\r\n\t" + str(node.getinnodes()))
        next = random.randint(0, len(possiblenodes) - 1)
        nextnode1 = possiblenodes[next]
        possiblenodes.remove(nextnode1)
        next = random.randint(0, len(possiblenodes) - 1)
        nextnode2 = possiblenodes[next]
        possiblenodes.remove(nextnode2)
        # While we're at it, add edges for nodes that beat our starting node
#        for n in possiblenodes:
#            n.addoutedge(Edge(n, node))
            
        if not(nextnode1 in self.outcompletenodes):
            self.nodestack.append(nextnode1)
        if not(nextnode2 in self.outcompletenodes):
            self.nodestack.append(nextnode2)

        node.addoutedge(Edge(node, nextnode1))
        nextnode1.addinnode(node)
        node.addoutedge(Edge(node, nextnode2))
        nextnode2.addinnode(node)

    def print(self):
        for node in self.nodes:
            print("Node:\t" + str(node))
            print("\t" + str(node.outedges))
            print("\t" + str(node.innodes))
            
            
def main():
    rpsgraph = Rgraph()
    rpsgraph.gennodes(5)
    rpsgraph.genedges()
    rpsgraph.print()
if __name__ == "__main__" : main()
