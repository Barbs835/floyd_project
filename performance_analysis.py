import sys
from timeit import default_timer as timer

import imperative_solution
import recursive_solution

no_path = sys.maxsize
    graph = [[0, 7, no_path, 8],
             [no_path, 0, 5, no_path],
             [no_path, no_path, 0, 2],
             [no_path, no_path, no_path, 0]]


if __name__ == '__main__':
   start = timer()
   x = [r for r in range(5000)]
   end = timer()
   print(end - start)

Result: 0.000846