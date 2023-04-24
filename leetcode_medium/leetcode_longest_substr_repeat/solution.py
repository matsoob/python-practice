# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = set()
        order = deque()
        longest_thus_far = 0
        # Iterating through once, so O_n
        for char in s:
            if char not in seen:
                seen.add(char)
                order.append(char)
                if longest_thus_far < len(seen):
                    longest_thus_far = len(seen)
            else:
                found_prev = False
                while not found_prev:
                    # here, we might pop off items within O_n loop
                    # The max number we pop off is the max different chars,
                    # which should be constant, so it can be considered constant time
                    removed = order.popleft()
                    if removed != char:
                        seen.remove(removed)
                    else:
                        found_prev = True
                order.append(char)
        # Space wise, uses the size of the longest unique substring
        # which is constrainted to the set() of English letters, digits, symbols and spaces;
        # So it can be considered constant space
        return longest_thus_far