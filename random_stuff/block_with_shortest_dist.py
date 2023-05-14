# https://www.youtube.com/watch?v=rw4s4M3hFfs
from typing import Any, List

input_1_1 = [
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": True,
        "school": False,
        "store": False
    },
    {
        "gym": True,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": True
    }
]
input_1_2 = [ "gym", "school", "store"]

def solve_me(input: List[Any], reqs: List[str]) -> int:
    n = len(input)
    # [True, False, False, False, True]
    # [0, 1, 2, 1, 0]
    max_distances = [0] * n
    for req in reqs:
        req_list = [ block[req] for block in input ]
        distance = [ None ] * n
        since_last_seen = None
        for i in range(n):
            if req_list[i]:
                distance[i] = 0
                since_last_seen = 0
            elif since_last_seen is not None:
                since_last_seen += 1
                distance[i] = since_last_seen
        
        since_last_seen = None
        for i in range(n-1, -1, -1):
            if req_list[i]:
                distance[i] = 0
                since_last_seen = 0
            elif since_last_seen is not None:
                since_last_seen += 1
                if distance[i] is not None:
                    distance[i] = min(distance[i], since_last_seen)
                else:
                     distance[i] = since_last_seen

        if None in distance:
            return -1

        for i in range(n):
            max_distances[i] = max(distance[i], max_distances[i])
        
    min_index = 0
    for i in range(1, n):
        if max_distances[min_index] > max_distances[i]:
            min_index = i
    return min_index

if __name__ == '__main__':
    assert solve_me(input_1_1, input_1_2) == 3