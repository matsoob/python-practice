# given a n*n matrix
# contains x's and o's
# capture all regions that are surrounded by x's in 4 directions
# 
# x x x x x
# o o o o o
# x x x o x
# x o o x x
# x x x x x

# - - - - -
# o o o o o

from collections import deque
from typing import List, Tuple


def capture_os(input: List[List[str]]):
    n = len(input)
    invincible_os = [[False] * n for _ in range(n)]
    queue = deque()
    for i in range(n):
        if input[0][i] == 'o':
            queue.append((0,i))
        if input[i][0] == 'o':
            queue.append((i,0))
        if input[n-1][i] == 'o':
            queue.append((n-1,i))
        if input[i][n-1] == 'o':
            queue.append((i,n-1))
    
    def get_neighbours(curr: Tuple[int, int]) -> List[Tuple[int, int]]:
        neighbours = list()
        if curr[0] > 0:
            if input[curr[0]-1][curr[1]] == 'o':
                neighbours.append((curr[0]-1, curr[1]))
        if curr[1] > 0:
            if input[curr[0]][curr[1]-1] == 'o':
                neighbours.append((curr[0], curr[1]-1))
        if curr[0] < n-1:
            if input[curr[0]+1][curr[1]] == 'o':
             neighbours.append((curr[0]+1, curr[1]))
        if curr[1] < n-1:
            if input[curr[0]][curr[1]+1] == 'o':
                neighbours.append((curr[0], curr[1]+1))
        return neighbours

    while queue:
        current = queue.popleft()
        invincible_os[current[0]][current[1]] = True
        neighbours = get_neighbours(current)
        for neighbour in neighbours:
            if not invincible_os[neighbour[0]][neighbour[1]]:
                queue.append(neighbour)

    for i in range(n):
        for j in range(n):
            if input[i][j] == 'o' and not invincible_os[i][j]:
                input[i][j] = 'x'
    for row in input:
        print(row)


input = [['x', 'x', 'x', 'x', 'x'],
        ['o', 'o', 'o', 'o', 'o'],
        ['x', 'x', 'x', 'o', 'x'],
        ['x', 'o', 'o', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'o']]

capture_os(input)