class graph:
    def __init__(self, V, E):
        self._struct = []
        self.vertex = []
        self.E = set(frozenset((u, v)) for u, v in E)
        for v in V:
            self.addVertex(v)
        for u, v in self.E:
            self.addEdge(u, v)

    def addVertex(self, v):
        if v not in self.vertex:
            self.vertex.append(v)
            if len(self.vertex) > 1:
                for i in self._struct:
                    i.append(0)
            temp = []
            for j in range(len(self.vertex)):
                temp.append(0)
            self._struct.append(temp)

    def addEdge(self, u, v):
        self.addVertex(u)
        self.addVertex(v)
        idx1 = self.vertex.index(u)
        idx2 = self.vertex.index(v)
        self._struct[idx1][idx2] = 1
        self._struct[idx2][idx1] = 1
        self.E.add(frozenset((u, v)))
    def degree(self, v):
        idx = self.vertex.index(v)
        return sum(self._struct[idx])

    def neighbours(self, v):
        idx = self.vertex.index(v)
        nbrs = []
        for i in range(len(self._struct[idx])):
            if self._struct[idx][i] == 1:
                nbrs.append(self.vertex[i])

        return nbrs

    def numVertex(self):
        return len(self.vertex)

    def numEdge(self):
        return len(self.E)

if __name__ == "__main__":
    g = graph([1, 2, 3, 4], {(1, 2),(2, 3), (1, 4), (2, 4 ), (4, 3)})
    print(g.degree(1))
    print(g.neighbours(1))
    print(g.numVertex())
    print(g.numEdge())
    g.addVertex(5)
    g.addVertex(6)
    g.addEdge(5, 3)
    g.addEdge(5, 2)
    g.addEdge(6, 1)
    g.addEdge(6, 5)
    print(g.neighbours(5))
    print(g.neighbours(6))








