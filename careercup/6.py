"""
->0 0 0 1 0 0
  0 0 1 0 0 0
  0 0 1 1 1 0<-
  0 0 0 0 0 0
"""

def bfs(grid, start, target):
    # Assume start and target are tuples of a pair of indices representing
    # positions on the grid.
    parent = {(start, 0): None}

    # Each element stored by the frontier consists of the position of the next
    # element to be explored as well as how many wall passes it has gone. This
    # means that there will be V * 4 total possible vertices to traverse, as
    # there may be more than one way to traverse a vertex (i.e. either through
    # a wall once, twice, three times, so on).
    frontier = [(start, 0)]
    next = []

    wall_flex = 0

    rowN = len(grid)
    colN = len(grid[0])

    path_found = False
    while frontier:
        for u in frontier:
            candidates = list()

            for c in range(4):
                if c == 0:
                    i, j = (u[0][0] - 1, u[0][1])
                elif c == 1:
                    i, j = (u[0][0] + 1, u[0][1])
                elif c == 2:
                    i, j = (u[0][0], u[0][1] - 1)
                elif c == 3:
                    i, j = (u[0][0], u[0][1] + 1)

                if (i >= 0 and i < rowN and j >= 0 and j < colN):
                    new_wall_flex = u[1] + grid[i][j]
                    if new_wall_flex <= wall_flex:
                        candidate = ((i, j), new_wall_flex)
                        if candidate not in parent:
                            if (i, j) == target:
                                parent[candidate] = u
                                path_found = True
                                break
                            else:
                                next.append(candidate)
                                parent[candidate] = u
            if path_found:
                break
        if path_found:
            break
        else:
            frontier = next
            next = []

    if path_found == True:
        for i in range(4):
            if (target, i) in parent:
                break
        # At this point, i is number of walls that was traversed in the
        # shortest path where up to 3 walls are possible to be traversed.
        path_element = (target, i)
        shortest_path = list()
        while path_element in parent:
            shortest_path.append(path_element[0])
            path_element = parent[path_element]
    return list(reversed(shortest_path)) if path_found else -1

grid = [[0, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 0],
[0, 0, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0]]

answer = bfs(grid, (0, 0), (2, 5))
print "Length of shortest path is %d" % (len(answer))
print answer
