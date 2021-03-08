# Dijkstra's single source shortest path algorithm

class Dijkstra:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def min_distance(self, dist, min_dist_set):
        min_dist = float("inf")
        for _v in range(self.vertices):
            if dist[_v] < min_dist and min_dist_set[_v] == False:
                min_dist = dist[_v]
                min_index = _v
        return min_index

    def dijkstra(self, src):

        dist = [float("inf")] * self.vertices
        dist[src] = 0
        min_dist_set = [False] * self.vertices

        for _ in range(self.vertices):

            # minimum distance vertex that is not processed
            _u = self.min_distance(dist, min_dist_set)

            # put minimum distance vertex in shortest tree
            min_dist_set[_u] = True

            # Update dist value of the adjacent vertices
            for _v in range(self.vertices):
                if self.graph[_u][_v] > 0 and min_dist_set[_v] == False and dist[_v] > dist[_u] + self.graph[_u][_v]:
                    dist[_v] = dist[_u] + self.graph[_u][_v]

        return dist
