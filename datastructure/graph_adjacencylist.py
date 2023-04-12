class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = set()

    def add_neighbor(self, vertex):
        self.neighbors.add(vertex)


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add_neighbor(vertex2)
            self.vertices[vertex2].add_neighbor(vertex1)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key, sorted(list(self.vertices[key].neighbors)))


if __name__ == '__main__':
    g = Graph()
    a = Vertex("A")
    g.add_vertex(a)
    g.add_vertex(Vertex('B'))
    for i in range(ord('A'), ord('G')):
        g.add_vertex(Vertex(chr(i)))

    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DF', 'EG', 'FG']
    for edge in edges:
        g.add_edge(edge[0], edge[1])

    g.print_graph()
