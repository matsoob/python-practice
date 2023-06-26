# https://leetcode.com/problems/combination-sum/
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]

from functools import lru_cache
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)

        @lru_cache()
        def recurse(remaining_list_index: int, curr_target: int) -> List[List[int]]:
            possibilities = list()
            if remaining_list_index >= len(candidates):
                return possibilities
            current_num = candidates[remaining_list_index]
            if current_num == curr_target:
                possibilities.append([current_num])
            if current_num < curr_target:
                # try using it
                remaining_target = curr_target - current_num
                possible_combos = recurse(remaining_list_index, remaining_target)
                for combo in possible_combos:
                    possibilities.append([current_num, *combo])
            # find all combos ahead of me
            possibilities.extend(recurse(remaining_list_index+1, curr_target))
            return possibilities

        return recurse(0, target)


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum([2,3,6,7], 7)) #[[2,2,3],[7]]
    print(sol.combinationSum([2,3,5],8))