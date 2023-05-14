
from collections import deque
from typing import List, Tuple


sample_input = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

sample_output = [
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

def removeIslands(matrix: List[List[int]]) -> List[List[int]]:
    # 1 -> black
    # 0 -> white
    # remove islands (blocks of black pixels unconnected to sides
    # diagonals don't count as adjacent
    n = len(matrix)
    to_explore = deque()
    visited = set()
    for i in range(n):
        if matrix[0][i] == 1:
            to_explore.append((0, i))
            visited.add((0, i))
        if matrix[n-1][i] == 1:
            to_explore.append((n-1, i))
            visited.add((n-1, i))
    for i in range(1, n-1):
        if matrix[i][0] == 1:
            to_explore.append((i, 0))
            visited.add((i, 0))
        if matrix[i][n-1] == 1:
            to_explore.append((i, n-1))     
            visited.add((i, n-1)) 

    def find_adjacent_black(me: Tuple[int, int]) -> List[Tuple[int, int]]:
        neighbours = list()
        x, y = me
        # up
        if x > 0:
            if matrix[x-1][y] == 1:
                neighbours.append((x-1, y))
        # down
        if x < n - 1:
            if matrix[x+1][y] == 1:
                neighbours.append((x+1, y))

        # left
        if y > 0:
            if matrix[x][y-1] == 1:
                neighbours.append((x, y-1)) 
        # right
        if y < n - 1:
            if matrix[x][y+1] == 1:
                neighbours.append((x, y+1))
        return neighbours

    while to_explore:
        curr = to_explore.popleft()
        neighbours = find_adjacent_black(curr)
        for neighbour in neighbours:
            if neighbour not in visited:
                visited.add(neighbour)
                to_explore.append(neighbour)
    
    # Now we have a list of land-connected places
    for i in range(n):
        for j in range(n):
            if (i, j) not in visited and matrix[i][j] == 1:
                matrix[i][j] = 0
    
    return matrix




if __name__ == '__main__':
    assert removeIslands(sample_input) == sample_output
