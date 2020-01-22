
from graph import Graph
from util import Stack

# step one: figure out how to relate the data in a graph:
"""
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9

    1 - { 3 }
    2 - { 3 }
    3 - { 6 }
    4 - { 5, 8 }
    5 - { 6, 7 }
    6 - { }
    7 - { }
    8 - { 9 }
    9 - { }
    10 - { 1 }
    11 - { 8 }

"""

# step two(rev):
# find all vertexes with connection to start-vert
# for each connection:
#   see if any connection to them
#   add to stack?

# target = int(start_vert)
# s = Stack()
# s.push(target)
# visited = set()
# for i in range(len(data))
#   if g.vertices[i+1] == target
# 
# 

# step two:
# start searching through the graph for a vertex with a connection to 6
# if conn:
#   set as new search-value
# else:
#   oldest ancestor -> return

# need to figure out how to follow multiple paths


def earliest_ancestor(ancestors, starting_node):
    # last in first out
    s = Stack()
    s.push(starting_node)
    
    path = []
    outer = []

    while s.size() > 0:
        # pop last in stack
        x = s.pop()
        # add current_node to path
        path.append(x)
        # iterate over verts to find all with children that match current_node(x)
        for i in range(len(ancestors.vertices)):
            print(i)
            # if edges at vert
            if ancestors.vertices[i+1]:
                # for each edge
                for vert in ancestors.vertices[i+1]:
                    if vert == x:
                        # s.push(vert)
                        # issue is here, I need to push i+1 to get vert
                        # target_vert = i+1
                        # s.push(target_vert)
            else:
                # no more ancestors -> add to outer list
                outer.append(path)
                # reset path
                path = []
    
    print("**", outer)

    # create a counter
    longest = []
    # for each path in list
    for i in range(len(outer)):
        # end of list
        if outer[i +1] is None:
            return longest
        # if two paths same num of ancestors
        if len(outer[i+1]) == len(outer[i]):
            # ↓ created to be able to capture last character
            next_path = i+1
            # if last val in next path is greater than last val in cur path
            if outer[i[-1]] < outer[next_path[-1]]:
                longest = path[i+1]
            else:
                longest = path[i]
        # if next path longer
        elif len(outer[i+1]) > len(outer[i]):
            longest = path[i+1]
    
    return longest[-1]

# test
a = Graph()
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y = [[3], [3], [6], [5, 8], [6, 7], [], [], [9], [], [1], [8]]

for i in x:
    a.add_vertex(i)

for i in range(len(y)):
    # print(i)
    for j in y[i]:
        a.add_edge(i+1, j)

# print(a.vertices)

print(earliest_ancestor(a, 6))
