
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
    8 - { 4, 11, 9 }
    9 - { 8 }
    10 - { 1 }
    11 - { 8 }

    or

    1 - { 3, 10 }
    2 - { 3 }
    3 - { 6, 1, 2 }
    4 - { 5, 8 }
    5 - { 4, 6, 7 }
    6 - { 3, 5 }
    7 - { 5 }
    8 - { 9 }
    9 - { }
    10 - { 1 }
    11 - { 8 }

    or

    1 - { 10 }
    3 - { 1, 2 }
    5 - { 4 }
    8 - { 4, 11 }
    6 - { 3, 5 }
    7 = { 5 }
    9 - { 8 }
"""

def earliest_ancestor(ancestors, starting_node):
    print(ancestors)
    g = Graph()

    # strip duplicates
    s = set()
    for pair in ancestors:
        for ancestor in pair:
            s.add(ancestor)
    l = list(s)

    # add to graph
    for num in l:
        g.add_vertex(num)
    
    # add ancestors
    for i in ancestors:
        g.add_edge(i[1], i[0])

    # last in first out
    s = Stack()
    s.push(starting_node)
    
    path = []
    outer = []
        
    # ---------------------

    while s.size() > 0:
        x = s.pop()
        path.append(x)

        if g.vertices[x]:
            for vert in g.vertices[x]:
                s.push(vert)
        # no ancestors to starting_node
        elif x == starting_node:
           return -1
        # reached the oldest ancestor for a path
        else:
            outer.append(path)
            path = path[:len(outer)]

    # create a counter
    longest = []
    # for each path in list
    for i in range(len(outer)):
        if len(outer[i]) > len(longest):
            longest = outer[i]
        elif len(outer[i]) == len(longest):
            x = outer[i]
            if x[-1] < longest[-1]:
                longest = x
    
    return longest[-1]

    # ---------------------

    # while s.size() > 0:
    #     # pop last in stack
    #     x = s.pop()
    #     # add current_node to path
    #     path.append(x)
    #     # iterate over verts to find all with children that match current_node(x)
    #     # needed to check if any vals found ie 4
    #     temp = []
    #     for i in range(len(ancestors.vertices)):
    #         print(i)
    #         # if edges at vert
    #         if ancestors.vertices[i+1]:
    #             # for each edge
    #             for vert in ancestors.vertices[i+1]:
    #                 print("!", vert, x)
    #                 if vert == x:
    #                     # s.push(vert)
    #                     # issue is here, I need to push i+1 to get vert
    #                     s.push(i+1)

    #     # add each path after
    #     outer.append(path)
    #     path = []
            
    # print("**", outer)

    # # create a counter
    # longest = []
    # # for each path in list
    # for i in range(len(outer)):
    #     # end of list
    #     if outer[i +1] is None:
    #         return longest
    #     # if two paths same num of ancestors
    #     if len(outer[i+1]) == len(outer[i]):
    #         # ↓ created to be able to capture last character
    #         next_path = i+1
    #         # if last val in next path is greater than last val in cur path
    #         if outer[i[-1]] < outer[next_path[-1]]:
    #             longest = path[i+1]
    #         else:
    #             longest = path[i]
    #     # if next path longer
    #     elif len(outer[i+1]) > len(outer[i]):
    #         longest = path[i+1]
    
    # return longest[-1]

# test
# a = Graph()
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# y = [[3], [3], [6], [5, 8], [6, 7], [], [], [9], [], [1], [8]]
# z = [[10], [], [1, 2], [], [4], [3, 5], [5], [4, 11], [8], [], []]

# for i in x:
#     a.add_vertex(i)

# for i in range(len(z)):
#     # print(i)
#     for j in z[i]:
#         a.add_edge(i+1, j)

# print(a.vertices)

# print(earliest_ancestor(a, 6))
