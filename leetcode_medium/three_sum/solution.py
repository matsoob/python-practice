# https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        found = list()
        # Naive-ish
        num_dict = dict()
        nums.sort()
        for i in range(len(nums)):
            num_dict[nums[i]] = i 
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                looking_for = 0 - nums[i] - nums[j]
                if looking_for in num_dict and num_dict[looking_for] > j:
                    found.append([nums[i], nums[j], looking_for])
        # still need to dedupe, plus it's n^2
   
        def silly_hash(figs: List[int]) -> str:
            return f'{figs[0]}{figs[1]}{figs[2]}'

        hashes = set()
        found_deduped = list()
        for f in found:
            hashed = silly_hash(f)
            if hashed not in hashes:
                hashes.add(hashed)
                found_deduped.append(f)

        return found_deduped

