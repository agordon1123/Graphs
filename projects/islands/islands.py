# Write a function that takes a 2D binary array and returns the number of 1 islands.
# An island consists of 1s that are connected to the north, south, east or west.
# For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

# connected - has edges, connected components
# array/2d - graph
# n, s, e, w - edges
# binary - values
# island/1 islands
# return 1 islands - number of connect components

from util import Queue, Stack

def get_neighbors(x, y, matrix):
    neighbors = []
    if x > 0 and matrix[y][x-1] == 1:
        # north
        neighbors.append((x-1, y))
    if x < len(matrix[0]) - 1 and matrix[y][x+1] == 1:
        # south
        neighbors.append((x+1, y))
    if y > 0 and matrix[y-1][x] == 1:
        # west
        neighbors.append((x, y-1))
    if y < len(matrix) - 1 and matrix[y+1][x] == 1:
        neighbors.append((x, y+1))
    return neighbors

def dfs(x, y, matrix, visited):
    s = Stack()
    s.push((x, y))
    while s.size() > 0:
        x = s.pop()
        if not visited[x[1]][x[0]]:
            visited[x[1]][x[0]] = True
            for neighbor in get_neighbors(x[0], x[1], matrix):
                s.push(neighbor)
    return visited


def island_counter(matrix):
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    island_count = 0
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if not visited[y][x]:
                if matrix[y][x] == 1:
                    visited = dfs(x, y, matrix, visited)
                    island_count += 1
                else:
                    visited[y][x] = True
    return island_count

def print_matrix(matrix):
    for row in matrix:
        print(''.join([str(i) for i in row]))

# TODO: create matrix to test
matrix = []
print_matrix(matrix)
island_counter(matrix)