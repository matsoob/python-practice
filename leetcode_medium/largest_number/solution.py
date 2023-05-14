# https://leetcode.com/problems/largest-number/
from typing import List, Set


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sorted_lists = [[]] * 10
        for i in nums:
            i_str = str(i)
            leading_digit = int(i_str[0])
            if sorted_lists[leading_digit]:
                sorted_lists[leading_digit].append(i_str)
            else:
                sorted_lists[leading_digit] = [i_str]
        for j in range(10):
            sorted_lists[j]
            if sorted_lists[j]:
                sorted_digs = self.orderByDigit(j, sorted_lists[j])
                sorted_lists[j] = sorted_digs

        result = ''
        for i in range(9, -1, -1):
            digs = sorted_lists[i]
            for dig in digs:
                result += str(dig)
        if int(result) == 0:
            return '0'
        return result

    # 334, 324, 330, 33, 3
    # -> 334, 33, 3, 330, 324
    def orderByDigit(self, leading_dig: int, ints: List[str]) -> List[int]:
        max_len = max([len(i) for i in ints])
        padded_int_pairs = [(f'{i.ljust(max_len, str(leading_dig))}', i) for i in ints]
        padded_int_pairs.sort(reverse=True)
        result = list()
        for pair in padded_int_pairs:
            result.append(pair[1])
        return result
    
    
    def largestNumber2(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x