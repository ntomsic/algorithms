# This class represents a directed graph using adjacency
class Graph:
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = {}

        # To store transitive closure
        self.tc = [[0 for j in range(self.V)] for i in range(self.V)]

    # function to add an edge to graph
    def add_edge(self, _u, _v):
        if _u in self.graph:
            self.graph[_u].append(_v)
        else:
            self.graph[_u] = [_v]

    # A recursive DFS traversal function that finds
    # all reachable vertices for s
    def dfs_util(self, _s, _v):

        # Mark reachability from s to v as true.
        self.tc[_s][_v] = 1

        # Find all the vertices reachable through v
        for i in self.graph[_v]:
            if self.tc[_s][i] == 0:
                self.dfs_util(_s, i)

    # The function to find transitive closure. It uses
    # recursive dfs_util()
    def transitive_closure(self):

        # Call the recursive helper function to print DFS
        # traversal starting from all vertices one by one
        for i in range(self.V):
            self.dfs_util(i, i)
        print(self.tc)

# g = Graph(4)
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.add_edge(2, 3)
# g.add_edge(3, 3)

# print("Transitive closure matrix is")
# g.transitive_closure()
