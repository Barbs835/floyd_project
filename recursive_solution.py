import sys
import itertools

no_path = sys.maxsize
distance_graph = [[0, 7, no_path, 8],
	             [no_path, 0, 5, no_path],
                 [no_path, no_path, 0, 2],
	             [no_path, no_path, no_path, 0]]

def floyd(distance):
	"""A simple implementation of Floyd's algorithm.
	The passed argument is 2D list.
	"""
	path = distance
	max_length = len(distance[0])

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

	# The floyd(distance) function starts by setting the start and end nodes,
	# that will be passed to the inner min_dist() recursive function.
	for start_node, end_node in itertools.product(range(max_length), range(max_length)):

		# If start_node and end_node are the same, then the distance would be zero.
		if start_node == end_node:
			distance[start_node][end_node] = 0
			continue
		# Update the distance graph with the shortest path values by calling the recursive
		# min_dist() function.
		distance[start_node][end_node] = min_dist(start_node, end_node, max_length - 1, path)
	# Print the 2D list with shortest paths.
	# Any value that have sys.maxsize has no path.
	return (distance)

# Calling the floyd() function
print(floyd(distance_graph))
