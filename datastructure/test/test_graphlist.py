import unittest
from datastructure.graphlist import Vertex, Graph


class TestGraphlist(unittest.TestCase):

    def test_add_empty(self):
        my_graph = Graph()
        result = my_graph.add_vertex(Vertex("A"))
        self.assertTrue(result)