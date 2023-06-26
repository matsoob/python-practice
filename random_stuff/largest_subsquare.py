# import numpy as np

def biggest_subsquare(a: list[list[int]]) -> int:
    """Returns the largest sub matrix of 1s."""
    n = len(a)
    columns = [[0]*n for _ in range(n)]
    rows = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                columns[i][j] = 0
                rows[i][j] = 0
            else:
                if i > 0:
                    columns[i][j] = columns[i-1][j] + 1
                else:
                    columns[i][j] = 1
                if j > 0:
                    rows[i][j] = rows[i][j-1] + 1
                else:
                    rows[i][j] = 1
    subsquares =  [[0]*n for i in range(n)]
    max_seen = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                subsquares[i][j] = 0
            else:
                if i == 0 or j == 0:
                    subsquares[i][j] = 1
                else:
                    new_square_size = min(rows[i][j], columns[i][j], subsquares[i-1][j-1]+1)
                    subsquares[i][j] = new_square_size
            max_seen = max(subsquares[i][j], max_seen)
    return max_seen
    

test_input = [
    [1, 0, 0, 1],
    [1, 1, 1, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 1]
]

test_input_2 = [
    [1, 0, 0, 1, 0], 
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0], 
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1]
]

test_input_3 = [
    [1, 0, 0, 1, 0], 
    [1, 1, 1, 1, 0],
    [1, 0, 1, 1, 0], 
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1]
]

if __name__ == '__main__':
    print(biggest_subsquare(test_input_3))
