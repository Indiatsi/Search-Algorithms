from heapq import heappush, heappop
from itertools import count

class BfsTraverser: 

        # Constructor 
        def __init__(self): 
                self.visited = []
                self.end_search = False
        def BFS(self,graph, start_node, goal_node):
                queue = []
                queue.append(start_node)
                #print(queue)
				#set of visited nodes
                self.visited.append(start_node)
                while queue and not self.end_search: 
                        # Dequeue a vertex from 
                        s = queue.pop(0) 
                        print ("Drive to" ,s, " Estate", end = "\n") 

                        # Get all adjacent vertices of the 
                        # dequeued vertex s. If a adjacent 
                        # has not been visited, then mark it 
                        # visited and enqueue it 
                        for i in list(graph[s]):
                                if i not in self.visited: 
                                    print("This is goal node ",goal_node," Current Node ",i)
                                    if i is goal_node:
                                        print(self.end_search)
                                        self.visited.append(i)
                                        self.end_search = True
                                        break
                                    else:
                                        print("hapa",self.end_search)
                                        queue.append(i)
                                        #visited[i] = True
                                        self.visited.append(i)
                #return visited
class ATraverser:
    # Constructor 
    def __init__(self): 
        self.explored = []
        self.end_search = False
    def astar_path(self,G,source,target,heuristic='heuristic',weight='weight'):
        if source not in G or target not in G:
            print('Either source', source, 'or target', target, 'is not in G')

        if heuristic is None:
            # The default heuristic is h=0 - same as Dijkstra's algorithm
            def heuristic(u, v):
                return 0
        

        push = heappush
        pop = heappop
    
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
        explored = {}

        while queue:
            _, __, curnode, dist, parent = pop(queue)
            if curnode == target:
                path = [curnode]
                node = parent
                while node is not None:
                    path.append(node)
                    node = explored[node]
                    path.reverse()
                    return path

                if curnode in explored:
                    # Do not override the parent of starting node
                    if explored[curnode] is None:
                        continue

                    # Skip bad paths that were enqueued before finding a better one
                    qcost, h = enqueued[curnode]
                    if qcost < dist:
                        continue

                explored[curnode] = parent

                for neighbor, w in G[curnode].items():
                    ncost = dist + w.get(weight, 1)
                    if neighbor in enqueued:
                        qcost, h = enqueued[neighbor]
                        # if qcost <= ncost, a less costly path from the
                        # neighbor to the source was already determined.
                        # Therefore, we won't attempt to push this neighbor
                        # to the queue
                        if qcost <= ncost:
                            continue
                        else:
                            h = heuristic(neighbor, target)
                            enqueued[neighbor] = ncost, h
                            push(queue, (ncost + h, next(c), neighbor, ncost, curnode))

            print("Node %s not reachable from %s" % (target, source))