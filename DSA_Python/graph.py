# Graph implementaion

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path = []):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def shortest_paths(self, start, end, path = []):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                s_path = self.shortest_paths(node, end, path)
                if shortest_path is None or len(s_path) < len(shortest_path):
                    shortest_path = s_path 
                

        return shortest_path

routes = [
    ('mumbai','paris'),
    ('mumbai','dubai'),
    ('paris','dubai'),
    ('paris','newyork'),
    ('dubai','paris'),
    ('dubai','newyork'),
    ('newyork','torrento'),
    ]


g = Graph(routes)

result = g.get_paths('mumbai', 'newyork')
print('All available paths :', result)
result2 = g.shortest_paths('mumbai', 'newyork')
print('Shortest path :', result2)



