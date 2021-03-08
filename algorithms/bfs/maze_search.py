from collections import deque

'''
BFS time complexity : O(|E| + |V|)
BFS space complexity : O(|E| + |V|)

do BFS from (0,0) of the grid and get the minimum number
of steps needed to get to the lower right column.

only step on the columns whose value is 1

if there is no path, it returns -1

Ex 1)
If grid is
[[1,0,1,1,1,1],
 [1,0,1,0,1,0],
 [1,0,1,0,1,1],
 [1,1,1,0,1,1]],
the answer is: 14

Ex 2)
If grid is
[[1,0,0],
 [0,1,1],
 [0,1,1]],
the answer is: -1
'''


def maze_search(maze):
    blocked, allowed = 0, 1
    unvisited, visited = 0, 1

    initial_x, initial_y = 0, 0

    if maze[initial_x][initial_y] == blocked:
        return -1

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    height, width = len(maze), len(maze[0])

    target_x, target_y = height - 1, width - 1

    queue = deque([(initial_x, initial_y, 0)])

    is_visited = [[unvisited for w in range(width)] for h in range(height)]
    is_visited[initial_x][initial_y] = visited

    while queue:
        _x, _y, steps = queue.popleft()

        if _x == target_x and _y == target_y:
            return steps

        for d_x, d_y in directions:
            new_x = _x + d_x
            new_y = _y + d_y

            if not (0 <= new_x < height and 0 <= new_y < width):
                continue

            if maze[new_x][new_y] == allowed and is_visited[new_x][new_y] == unvisited:
                queue.append((new_x, new_y, steps + 1))
                is_visited[new_x][new_y] = visited

    return -1
