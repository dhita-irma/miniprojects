# A Maze is given as N*N binary matrix of blocks where source block is the upper left most block i.e., maze[0][0]
# and destination block is lower rightmost block i.e., maze[N-1][N-1]

# A rat starts from source and has to reach the destination.
# The rat can move only in two directions: forward and down.

# In the maze matrix, 0 means the block is a dead end and
# 1 means the block can be used in the path from source to destination.

# Algorithm:
# Create a solution matrix, initially filled with 0’s.
# Create a recursive function, which takes initial matrix, output matrix and position of rat (i,j).
# if the position is out of the matrix or the position is not valid then return.
# Mark the position output[i][j] as 1 and Check if the current position is destination or not.
# If destination is reached print the output matrix and return.
# Recursively call for position (i+1,j) and (i,j+1).
# Unmark position (i,j), i.e output[i][j] = 0



def print_solution(sol):
    for i in sol:
        for j in i:
            print(str)