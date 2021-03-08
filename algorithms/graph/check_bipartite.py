"""

Bipartite graph is a graph whose vertices can be divided into two disjoint and independent sets.
(https://en.wikipedia.org/wiki/Bipartite_graph)

Time complexity is O(|E|)
Space complexity is O(|V|)

"""


def check_bipartite(adj_list):
    V = len(adj_list)

    # Divide vertexes in the graph into set_type 1 and 2
    # Initialize all set_types as -1
    set_type = [-1 for v in range(V)]
    set_type[0] = 0

    _q = [0]

    while _q:
        v = _q.pop(0)

        # If there is a self-loop, it cannot be bipartite
        if adj_list[v][v]:
            return False

        for _u in range(V):
            if adj_list[v][_u]:
                if set_type[_u] == set_type[v]:
                    return False
                if set_type[_u] == -1:
                    # set type of u opposite of v
                    set_type[_u] = 1 - set_type[v]
                    _q.append(_u)

    return True
