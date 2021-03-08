from collections import defaultdict


class Graph:
    def __init__(self, _v):
        self.v = _v
        self.graph = defaultdict(list)

    def add_edge(self, _u, _v):
        self.graph[_u].append(_v)

    def dfs(self):
        visited = [False] * self.v
        self.dfs_util(0, visited)
        if visited == [True] * self.v:
            return True
        return False

    def dfs_util(self, i, visited):
        visited[i] = True
        for _u in self.graph[i]:
            if not visited[_u]:
                self.dfs_util(_u, visited)

    def reverse_graph(self):
        _g = Graph(self.v)
        for i in range(len(self.graph)):
            for j in self.graph[i]:
                _g.add_edge(j, i)
        return _g

    def is_sc(self):
        if self.dfs():
            g_r = self.reverse_graph()
            if g_r.dfs():
                return True
        return False


g1 = Graph(5)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
g1.add_edge(3, 0)
g1.add_edge(2, 4)
g1.add_edge(4, 2)
print("Yes") if g1.is_sc() else print("No")

g2 = Graph(4)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 3)
print("Yes") if g2.is_sc() else print("No")
