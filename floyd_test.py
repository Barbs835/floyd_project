import unittest
import sys

from recursive_solution import floyd

# Testing the floyd function.
class TestFloyd(unittest.TestCase):
    # Define method of testing.
    def test_floyd(self):
        no_path = sys.maxsize
        graph_1 = [[0, 7, no_path, 8],
                   [no_path, 0, 5, no_path],
                   [no_path, no_path, 0, 2],
                   [no_path, no_path, no_path, 0]]

        shortest_dist = [[0, 7, 12, 8],
                         [no_path, 0, 5, 7],
                         [no_path, no_path, 0, 2],
                         [no_path, no_path, no_path, 0]]

        result = floyd(graph_1)
        self.assertEqual(result, shortest_dist)

    def test_various_arguments(self):
        no_path = sys.maxsize

        self.assertEqual(floyd([[4]]), [[0]])
        self.assertEqual(floyd([[no_path]]), [[0]])
        self.assertEqual(floyd([["str"]]), [[0]])

    if __name__ == '__main__':
        unittest.main()
