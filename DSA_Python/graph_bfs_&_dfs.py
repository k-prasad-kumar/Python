# BFS Algorithm implementation


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    
    def bfs(self, startNode):
        # visited = [False] * self.graph_dict   #if its graph_dict have int keys
        visited = set()
        queue = []
        visited.add(startNode)
        queue.append(startNode)

        while queue:
            startNode = queue.pop(0)

            for i in self.graph_dict[startNode]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
        return visited


    def dfs(self,start, visited = set()):
        visited.add(start)

        for node in self.graph_dict[start]:
            if node not in visited:
                self.dfs(node, visited)

        return visited
                
        
routes = [
    ('mumbai','paris'),
    ('mumbai','dubai'),
    ('paris','dubai'),
    ('paris','newyork'),
    ('dubai','paris'),
    ('dubai','newyork'),
    ('newyork','torrento'),
    ('torrento','newyork'),
    ]

g = Graph(routes)

result = g.bfs('mumbai')
print('BFS :', result)


print('DFS :', g.dfs('dubai'))


