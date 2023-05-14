def find_sum_of_three(nums, target):
   # Replace this placeholder return statement with your code
   sorted_nums = sorted(nums)  # O_nlogn
   
   for i in range(len(sorted_nums) - 2): # O_n^2
      num = sorted_nums[i]
      left = i + 1
      right = len(sorted_nums) - 1
      remaining_target = target - num
      while left < right:
        if sorted_nums[left] + sorted_nums[right] == remaining_target:
            return True
        elif sorted_nums[left] + sorted_nums[right] < remaining_target:
            left += 1
        else:
            right -= 1
   return False
