"""
Implements Tarjan's algorithm for finding strongly connected components
in a graph.
https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
"""
from algorithms.graph.graph import DirectedGraph


class Tarjan(object):
    def __init__(self, dict_graph):
        self.graph = DirectedGraph(dict_graph)
        self.index = 0
        self.stack = []

        # Runs Tarjan
        # Set all node index to None
        for _v in self.graph.nodes:
            _v.index = None

        self.sccs = []
        for _v in self.graph.nodes:
            if _v.index is None:
                self.strongconnect(_v, self.sccs)

    def strongconnect(self, _v, sccs):
        # Set the depth index for v to the smallest unused index
        _v.index = self.index
        _v.lowlink = self.index
        self.index += 1
        self.stack.append(_v)
        _v.on_stack = True

        # Consider successors of v
        for _w in self.graph.adjmt[_v]:
            if _w.index is None:
                # Successor w has not yet been visited; recurse on it
                self.strongconnect(_w, sccs)
                _v.lowlink = min(_v.lowlink, _w.lowlink)
            elif _w.on_stack:
                # Successor w is in stack S and hence in the current SCC
                # If w is not on stack, then (v, w) is a cross-edge in the DFS tree and is ignored
                # Note: The next line may look odd - but is correct.
                # It says w.index not w.lowlink; that is deliberate and from the original paper
                _v.lowlink = min(_v.lowlink, _w.index)

        # If v is a root node, pop the stack and generate an SCC
        if _v.lowlink == _v.index:
            # start a new strongly connected component
            scc = []
            while True:
                _w = self.stack.pop()
                _w.on_stack = False
                scc.append(_w)
                if _w == _v:
                    break
            scc.sort()
            sccs.append(scc)
