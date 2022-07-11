
from timeit import default_timer as timer

if __name__ == '__main__':
   start = timer()
   x = [r for r in range(5000)]
   end = timer()
   print(end - start)

Result: 0.000846