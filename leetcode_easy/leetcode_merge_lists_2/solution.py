# https://leetcode.com/problems/merge-sorted-array/

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # first, lazy approach with worse space complexity
        one_pointer = 0
        copy_pointer = 0
        two_pointer = 0
        copy_of_one = nums1.copy()
        while two_pointer < n or copy_pointer < m:
            if two_pointer == n:
                nums1[one_pointer] = copy_of_one[copy_pointer]
                copy_pointer += 1         
            elif copy_pointer == m: 
                nums1[one_pointer] = nums2[two_pointer]
                two_pointer += 1
            elif nums2[two_pointer] < copy_of_one[copy_pointer]:
                nums1[one_pointer] = nums2[two_pointer]
                two_pointer += 1
            else:
                nums1[one_pointer] = copy_of_one[copy_pointer]
                copy_pointer += 1
            one_pointer += 1

    # def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     one_pointer = 0
    #     two_pointer = 0
    #     curr_temp_head = None
    #     curr_temp_pointer = None
    #     while one_pointer < n+m:
    #         if curr_temp_head and curr_temp_head > curr_temp_pointer:
    #             raise Exception
    #         if one_pointer >= m and two_pointer >= n:
    #             nums1[one_pointer] = nums1[curr_temp_head]
    #             one_pointer += 1
    #             curr_temp_head += 1
    #         elif one_pointer >= m:
    #             if nums1[curr_temp_head] < nums2[two_pointer]:
    #                 nums1[one_pointer] = nums1[curr_temp_head]
    #                 one_pointer += 1
    #                 curr_temp_head += 1
    #             else:
    #                 nums1[one_pointer] = nums2[two_pointer]
    #                 one_pointer += 1
    #                 two_pointer += 1
    #         elif two_pointer >=n:
    #             if curr_temp_head > curr_temp_pointer:
    #                 raise
    #             nums1[one_pointer] = nums1[curr_temp_head]
    #             one_pointer += 1
    #             curr_temp_pointer += 1
    #         else:
    #             if nums1[one_pointer] < nums2[two_pointer]:
    #                 temp = nums1[one_pointer]
    #                 nums1[one_pointer] = nums1[curr_temp_head]
    #                 nums1[curr_temp_pointer] = temp
    #                 one_pointer += 1
    #                 curr_temp_head += 1
    #                 curr_temp_pointer += 1
    #             else:
    #                 temp = nums1[one_pointer]
    #                 nums1[one_pointer] = nums2[two_pointer]
    #                 nums1[curr_temp_pointer] = temp
    #                 one_pointer += 1
    #                 two_pointer += 1
    #                 curr_temp_pointer += 1
    #         print('after step')
    #         print(nums1)
    #         print(nums2)
        
            

    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        one_pointer = n + m - 1
        curr_one_tail = m - 1
        curr_two_tail = n - 1
        while one_pointer >= 0:
            if curr_one_tail >= 0 and \
                (curr_two_tail < 0 or nums1[curr_one_tail] > nums2[curr_two_tail]):
                nums1[one_pointer] = nums1[curr_one_tail]
                one_pointer -= 1
                curr_one_tail -= 1
            else:
                nums1[one_pointer] = nums2[curr_two_tail]
                one_pointer -= 1
                curr_two_tail -= 1
