import unittest
from datastructure.graph_adjacencylist import Vertex, Graph


class TestGraphlist(unittest.TestCase):

    def test_add_empty(self):
        my_graph = Graph()
        result = my_graph.add_vertex(Vertex("San Francisco"))
        self.assertTrue(result)