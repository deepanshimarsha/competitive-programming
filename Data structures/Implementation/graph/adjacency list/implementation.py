class Graph:
    def __init__(self, V, E):
        #make unordered pair of edges
        self.E = set(frozenset((u, v)) for u, v in E)
        self._struct = {}
        for v in V:
            self.addVertex(v)
        for u,v in self.E:
            self.addEdge(u,v)

    def addVertex(self, v):
        if v not in self._struct:
            self._struct[v] = set()

    def addEdge(self, u, v):
        self.addVertex(u)
        self.addVertex(v)
        self._struct[u].add(v)
        self._struct[v].add(u)
        self.E.add(frozenset((u, v)))

    def degree(self, v):
        return len(self._struct[v])

    def neighbours(self, v):
        return self._struct[v]

    def numEdges(self):
        return len(self.E)

    def numVertex(self):
        return len(self._struct)

if __name__ == "__main__":
    g = Graph([1, 2, 3], {(1, 2), (2, 3)})
    print(g.neighbours(3))
    print(g.numEdges())
    g.addVertex(4)
    g.addEdge(4, 3)
    print(g.neighbours(4))
    print(g.numEdges())
    print(g.numVertex())




