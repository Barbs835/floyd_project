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
   recursive_solution.floyd(graph)
   end = timer()
   dur1 = (end - start)
   format_str1 = "It took %f seconds to execute Recursive solution"


   start = timer()
   imperative_solution.floyd(graph)
   end = timer()
   dur2 = (end - start)
   format_str2 = "It took %f seconds to execute Imperative solution"

   print(format_str1 % dur1)
   print(format_str2 % dur2)