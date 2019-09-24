from heapq import heappush as push, heappop as pop
from itertools import count


class ATraverser:
    # Constructor
    def __init__(self):
        self.explored = {}
        self.end_search = False

    def astar_path(self, G, source, target, heuristic='heuristics', weight='weight'):
        if source not in G or target not in G:
            raise ValueError('Either source', source,
                             'or target', target, 'is not in G')

        # if heuristic is None:
        #     # The default heuristic is h=0 - same as Dijkstra's algorithm
        #     def heuristic(u, v):
        #         return 0
        # !! ALTERED VERSION MOVED DOWN

        # !!  SET IN THE IMPORT STATEMENT
        # push = heappush
        # pop = heappop

        # The queue stores priority, node, cost to reach, and parent.
        # Uses Python heapq to keep in priority order.
        # Add a counter to the queue to prevent the underlying heap from
        # attempting to compare the nodes themselves. The hash breaks ties in the
        # priority and is guaranteed unique for all nodes in the graph.
        c = count()
        queue = [(0, next(c), source, 0, None)]

        # Maps enqueued nodes to distance of discovered paths and the
        # computed heuristics to target. We avoid computing the heuristics
        # more than once and inserting the node into the queue too many times.
        enqueued = {}
        # Maps explored nodes to parent closest to the source.
        # explored = {} !! WAS INITIALISED IN CLASS

        while queue:
            _, __, curnode, dist, parent = pop(queue)
            if curnode == target:
                self.explored[curnode] = parent
                path = [curnode]
                node = parent
                while node is not None:
                    path.append(node)
                    node = self.explored[node]
                path.reverse()  # Reverse after exiting the loop
                return path

            if curnode in self.explored:
                # Do not override the parent of starting node
                if self.explored[curnode] is None:
                    print("He")
                    continue

                # Skip bad paths that were enqueued before finding a better one
                qcost, h = enqueued[curnode]
                if qcost < dist:
                    continue

            self.explored[curnode] = parent

            for neighbor, w in G[curnode].items():
                # !! WEIGHT IS SET AS STRING, SO TYPE CAST
                ncost = dist + float(w.get(weight, 1))
                # Check if not in queue and not explored
                if neighbor not in enqueued and neighbor not in list(self.explored.keys()):
                    h = 0 if heuristic is None else G.node[neighbor][heuristic]
                    enqueued[neighbor] = ncost, h
                    push(queue, (ncost + h, next(c),
                                 neighbor, ncost, curnode))
                elif neighbor in enqueued:
                    qcost, h = enqueued[neighbor]
                    # if qcost <= ncost, a less costly path from the
                    # neighbor to the source was already determined.
                    # Therefore, we won't attempt to push this neighbor
                    # to the queue
                    if qcost <= ncost:
                        continue
                    else:
                        h = 0 if heuristic is None else G.node[neighbor][heuristic]
                        enqueued[neighbor] = ncost, h
                        push(queue, (ncost + h, next(c),
                                    neighbor, ncost, curnode))