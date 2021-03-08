from collections import defaultdict


class Graph:
    def __init__(self, _v):
        self.v = _v
        self.graph = defaultdict(list)
        self.has_path = False

    def add_edge(self, _u, _v):
        self.graph[_u].append(_v)

    def dfs(self, _x, _y):
        visited = [False] * self.v
        self.dfsutil(visited, _x, _y, )

    def dfsutil(self, visited, _x, _y):
        visited[_x] = True
        for i in self.graph[_x]:
            if _y in self.graph[_x]:
                self.has_path = True
                return
            if not visited[i]:
                self.dfsutil(visited, _x, i)

    def is_reachable(self, _x, _y):
        self.has_path = False
        self.dfs(_x, _y)
        return self.has_path


# Create a graph given in the above diagram
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

U = 1
V = 3

if g.is_reachable(U, V):
    print("There is a path from %d to %d" % (U, V))
else:
    print("There is no path from %d to %d" % (U, V))

U = 3
V = 1
if g.is_reachable(U, V):
    print("There is a path from %d to %d" % (U, V))
else:
    print("There is no path from %d to %d" % (U, V))
