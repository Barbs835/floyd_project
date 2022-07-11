import unittest
import sys

from min_dist_function import min_dist

# Test the minimum distnace recursive function
class MinDistTestCase(unittest.TestCase):


    def test_min_dist(self):
        no_path = sys.maxsize
        graph = [[0, 7, no_path, 8],
                [no_path, 0, 5, no_path],
                [no_path, no_path, 0, 2],
                [no_path, no_path, no_path, 0]]
        # Calculate the shortest path from node 0 to node 2
        # whilst iterating through intermediate node k
        self.assertEqual(min_dist(0, 2, 3, graph), 12)
        # Calculate the shortest path from node  1 to node 2
        # when node k = -1
        self.assertEqual(min_dist(1, 2, -1, graph), 5)
        # Calculate the shortest path from node  3 to node 3
        # when node k = 0
        self.assertEqual(min_dist(3, 3, 0, graph), 0)
        # Calculate the shortest path from node  0 to node 0
        # when intermediate node k = 0
        # Please note that this inner function does not have assumption
        # that when start node = end node, distance is zero
        self.assertEqual(min_dist(0, 0, 0, [[2]]), 2)

if __name__ == '__main__':
    unittest.main()
