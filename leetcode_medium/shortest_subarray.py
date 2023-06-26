# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

from typing import List


class Solution:
    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        first_divergence = None
        last_divergence = None
        for i, n in enumerate(nums):
            if sorted_nums[i] != n:
                if first_divergence is None:
                    first_divergence = i
                last_divergence = i
        if first_divergence is None:
            return 0 
        else:
            return last_divergence - first_divergence + 1
        # stack = list()
        # deepest_unwind = float('inf')
        # most_recent_unwind = None
        # for n in nums:
        #     if not stack or stack[-1] <= n:
        #         stack.append(n)
        #     else:
        #         most_recent_unwind = len(stack)
        #         unwind = list()
        #         while stack and stack[-1] > n:
        #             unwind.append(stack.pop())
        #         deepest_unwind = min(len(stack), deepest_unwind)
        #         stack.append(n)
        #         while unwind:
        #             stack.append(unwind.pop())
        
        # if most_recent_unwind is None:
        #     return 0
        # else:
        #     return most_recent_unwind - deepest_unwind + 1

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = list()
        deepest_unwind = float('inf')
        most_recent_unwind = None
        for i, n in enumerate(nums):
            if not stack or stack[-1] <= n:
                stack.append(n)
            else:
                most_recent_unwind = i
                while stack and stack[-1] > n:
                    stack.pop()
                deepest_unwind = min(len(stack), deepest_unwind)
                stack.append(n)
        
        if most_recent_unwind is None:
            return 0
        else:
            return most_recent_unwind - deepest_unwind + 1
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.findUnsortedSubarray([2,6,4,8,10,9,15]))
    print(sol.findUnsortedSubarray([1,2,3,4]))
