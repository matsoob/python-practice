from typing import List


def circular_array_loop(nums: List[int]):  
    # Naive first
    n = len(nums)
    if not nums or len(nums) == 1:
        return True
    current_root = 0
    while current_root < n:
        if nums[current_root] == 0:
            return True
        is_positive = nums[current_root] > 0
        pointer = (current_root + nums[current_root]) % n
        
        while 


    
    pass


if __name__ == '__main__':
    test_cases = [
        ([1,3,-2,-4,1], True)
    ]
    for input, output in test_cases:
        assert circular_array_loop(input) == output