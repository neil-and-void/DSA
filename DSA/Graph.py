class Vertex:
    def __init__(self, key):
        self.key = key
        self.edges = dict()

    def addNeighbor(self, nbr, weight):
        self.edges[nbr] = weight

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        pass

    def addEdge(self, fromNode, toNode, ):
        if fromNode not in self.numVertices:
            pass

