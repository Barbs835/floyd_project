# Floyd Warshall Algorithm
## Using Python Recursive Function

### Project Description 
Floyd’s algorithm finds a shortest path distance between two nodes on a graph. This code replaces loop with recursive function and is a re-written version of Python imperative solution which shows a simple implementation of Floyd’s algorithm and returns a graph matrix. 
The solution picks a node and then calculates the distance between every start and end node. It also includes the intermediate node as part
of the indirect path. Then it compares distances of direct and indirect paths between given start and end nodes and selects the shortest path and updates the distance graph accordingly.

### How to Install and Run the Project
Required installation packages are listed in the following file:
```
requirements.txt
```

The main code is in the following gfile:
```
recursive_solution.py
```
It can be either copied (the raw content of the file) or the entire floyd_project repo  cloned to the local repository.


### Test
Python unittest library is used to run basic test cases for the floyd algorithm function and recursive function min_dist().
Test files are as follows:
```
 min_dist_function_test.py 
 floyd_test.py
```

### Credits
This code is based on the Floyd Warshall Algorithm (Imperative Solution) sourced from University of Liverpool assignment paper as well as GeeksforGeeks post available at: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/

### License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Copyright (c) 2022 Barbara
