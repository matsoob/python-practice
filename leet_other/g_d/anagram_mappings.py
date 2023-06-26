
from collections import defaultdict
from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num2_dict = defaultdict(list)
        for i, num in enumerate(nums2):
            num2_dict[num].append(i)
        result = list()
        for num in nums1:
            result.append(num2_dict[num].pop())

        return result
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.anagramMappings([84,46], [84,46]))
    print(sol.anagramMappings([12,28,46,32,50], [50,12,32,46,28])) 