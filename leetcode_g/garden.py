from collections import defaultdict, deque
from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        edge_dict = defaultdict(list)
        for path in paths:
            edge_dict[path[0]].append(path[1])
        cant_plant_map = defaultdict(list)
        result = [0] * n
        result[0] = 1
        current_pointer = 0
        to_colour = deque()
        