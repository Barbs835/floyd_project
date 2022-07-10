import sys
import itertools

no_path = sys.maxsize
distance_graph = [[0, 7, no_path, 8],
	             [no_path, 0, 5, no_path],
                 [no_path, no_path, 0, 2],
	             [no_path, no_path, no_path, 0]]


def min_dist(i, j, k, graph):
	"""Inner recursive function finding shortest path distance between start
	and end nodes.
			Key arguments:
			i -- start node
			j -- end node
			k -- intermediate node
			graph -- 2D list
			"""
	# If the path between i and j nodes is direct and does not go through
	# intermediate k node, return the direct path, otherwise find the
	# shortest distance between direct and indirecte paths.
	if k == -1:
		return(graph[i][j])
	else:
		return min(min_dist(i, j, k - 1, graph),
				   min_dist(i, k, k - 1, graph)
				   + min_dist(k, j, k - 1, graph))