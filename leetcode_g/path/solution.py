# https://leetcode.com/problems/number-of-good-paths/

from typing import List


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        pass

if __name__ == '__main__':
    sol = Solution()
    assert sol.numberOfGoodPaths([1,3,2,1,3], [[0,1],[0,2],[2,3],[2,4]]) == 6