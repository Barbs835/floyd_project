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

	# floyd function will generate base nodes (start, end) using intertools.product()
	# that will be passed to the recursive inner function min_dist()




	# REMINDER: DO NOT USE draft code from last Friday (check mid_assign_corrected folder)

	# INNER FUNCTIONS goes here...............................

	# recursive inner function, which will iterate through k (intermdiate node)
	# and find the shortest path values.



# These values will be used to update the outcome graph for shortest distances in
# the floyd function