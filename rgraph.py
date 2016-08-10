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
    def __init__(self, name, degree):
        self.name = name
        self.degree = degree
    def __str__(self):
        return "Node Name:\t" + self.name + "\r\nNode Degree:\t" + str(self.degree)
    def __repr__(self):
        return self.__str__()
    def addoutedge(self, edge):
        if not(edge in self.outedges):
            self.outedges.append(edge)
    def addinedge(self, edge):
        if not(edge in self.inedges):
            self.inedges.append(edge)
    def iscomplete(self):
        if len(self.outedges) + len(self.inedges) == self.degree:
            return True
        return False
class Rgraph(object):    
    nodes = []
    def gennodes(self, numnodes):
        for i in range(0, numnodes):
            self.nodes.append(Node(str(i), numnodes - 1))
            print(self.nodes[i])

    def choosenextnode(self, startnode):
        next = random.randint(0, len(self.nodes) - 1)
        while next == startnode:
            next = random.randint(0, len(self.nodes) - 1)
        return next
    
    def genedges(self):
        # Need to have n/2 out edges and n/2 in edges
        completednodes = []
        startnode = random.randint(0, len(self.nodes) - 1)
        while len(completednodes) != len(self.nodes):
            node = self.nodes[startnode]
            next = self.choosenextnode(node)
            nextnode = self.nodes[next]
            node.addoutedge(Edge(node, nextnode))
            if node.iscomplete() == True:
                completednodes.append(node)
            startnode = next

    def print(self):
        for node in nodes:
            print(node)
            print("\t" + node.outedges)
            print("\t" + node.inedges)
            
            
def main():
    rpsgraph = Rgraph()
    rpsgraph.gennodes(5)
    rpsgraph.genedges()
    rpsgraph.print()
if __name__ == "__main__" : main()
