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