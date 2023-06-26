# https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if not s:
            return 0
        sub_start = 0
        sub_end = 1
        current_longest = 1
        already_a_pair = False
        while sub_end < len(s):
            if s[sub_end - 1] is s[sub_end]:
                if not already_a_pair:
                    already_a_pair = True
                else:
                    while already_a_pair:
                        if s[sub_start] is s[sub_start + 1]:
                            already_a_pair = False
                        sub_start += 1
                    already_a_pair = True
            current_longest = max(sub_end - sub_start + 1, current_longest)
            sub_end += 1
        return current_longest
                    



    # misunderstood the question theree
    # def longestSemiRepetitiveSubstring(self, s: str) -> int:
    #     if not s:
    #         return 0
        
    #     sub_start = 0
    #     sub_end = 0
    #     current_longest = 0
    #     seen = set()
    #     current_pair = None
    #     while sub_end < len(s):
    #         char = s[sub_end]
    #         print('adding ', char)
    #         if char not in seen:
    #             seen.add(char)
    #         elif char in seen:
    #             if current_pair is None:
    #                 current_pair = char
    #             else:
    #                 while current_pair is not None and char in seen:
    #                     print('unwinding')
    #                     print('currently ', sub_start)
    #                     print('current_pair ', current_pair)
    #                     head_char = s[sub_start]
    #                     if head_char is current_pair:
    #                         current_pair = None
    #                     else:
    #                         seen.remove(head_char)
    #                     sub_start += 1
    #                 if char in seen:
    #                     current_pair = char
    #                 else:
    #                     seen.add(char)
    #         current_longest = max(current_longest, sub_end - sub_start + 1)
    #         sub_end += 1
    #     return current_longest
