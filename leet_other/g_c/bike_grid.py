from functools import lru_cache
from typing import List


class Solution:
    
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n = len(workers)
        m = len(bikes)
        @lru_cache()
        def get_distance(worker: int, bike: int) -> int:
            w_coords = workers[worker]
            b_coords = bikes[bike]
            return abs(w_coords[0] - b_coords[0]) + abs(w_coords[1] - b_coords[1])
        
        bikes_taken = [False]*m
        def backtracking(curr_worker: int) -> int:
            if curr_worker == n:
                return 0
            min_distance = None
            for bike in range(m):
                if not bikes_taken[bike]:
                    bikes_taken[bike] = True
                    min_for_this_assignment = get_distance(curr_worker, bike) + backtracking(curr_worker+1)
                    min_distance = min_for_this_assignment if min_distance is None else min(min_distance, min_for_this_assignment)
                    bikes_taken[bike] = False
            return min_distance
        return backtracking(0)
            
    def assignBikes2(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n = len(workers)
        m = len(bikes)
        @lru_cache()
        def get_distance(worker: int, bike: int) -> int:
            w_coords = workers[worker]
            b_coords = bikes[bike]
            return abs(w_coords[0] - b_coords[0]) + abs(w_coords[1] - b_coords[1])

        bikes_taken_by = [None]*m

        def get_current_total_distance() -> int:
            total_distance = 0
            for i, taken_by in enumerate(bikes_taken_by):
                if taken_by is not None:
                    total_distance += get_distance(taken_by, i)
            return total_distance

        def backtracking(curr_worker: int) -> int:
            if curr_worker == n:
                return get_current_total_distance()
            min_distance = None
            for bike in range(m):
                if bikes_taken_by[bike] is None:
                    bikes_taken_by[bike] = curr_worker
                    curr_distance = get_current_total_distance()
                    if min_distance is None or curr_distance < min_distance:
                        min_for_this_assignment = backtracking(curr_worker+1)
                        min_distance = min_for_this_assignment if min_distance is None else min(min_distance, min_for_this_assignment)
                    bikes_taken_by[bike] = None
            return min_distance
        return backtracking(0)

sol = Solution()
print(sol.assignBikes([[0,0],[2,1]], [[1,2],[3,3]])) # expect 6
print(sol.assignBikes([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]])) # expect 4
print(sol.assignBikes([[0,0],[1,0],[2,0],[3,0],[4,0]], [[0,999],[1,999],[2,999],[3,999],[4,999]])) 
print(sol.assignBikes2([[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]],[[0,999],[1,999],[2,999],[3,999],[4,999],[5,999],[6,999],[7,999],[8,999],[9,999]]))
# expect 4995