
# Write a function that takes a 2D binary array and returns the number of 1 islands.
# An island consists of 1s that are connected to the north, south, east or west.
# For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

# connected - has edges, connected components
# array/2d - graph
# n, s, e, w - edges
# binary - values
# island/1 islands
# return 1 islands - number of connect components

connected_components = []

for v in graph.vertexes:
    v.color = white

for v in graph.vertexes:
    if v.color == white:
        component = bfs(v)
        connected_components.push(component)


for i in range(len(islands)):
    for j in i:
        # if prior list
        if islands[i-1]:
            # north
            if islands[i-1][i] == 1:
                # add to connected component
        if islands[i+1]:
            # south
            if islands[i+1][i] == 1:
                # add to connected component
        if islands[i][i-1]:
            # west
            if islands[i][i-1] == 1:
                # add to connected component
        if islands[i][i+1]:
            # west
            if islands[i][i+1] == 1:
                # add to connected component
    # todo: need to track when all visited and none in any direction
