# https://leetcode.com/problems/decode-ways/
class Solution:
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        set_of_strs = set([ str(i) for i in range(1, 27)])
        ways_to_split = [0] * len(s)
        pointer = 0
        while pointer < len(s):
            if pointer == 0:
                if s[pointer] in set_of_strs:
                    ways_to_split[pointer] = 1
            else:
                one_char_option = 0
                two_char_option = 0
                if s[pointer] in set_of_strs:
                    one_char_option = ways_to_split[pointer-1]
                if s[pointer-1:pointer+1] in set_of_strs:
                    two_char_option = ways_to_split[pointer-2] if pointer-2 >= 0 else 1
                ways_to_split[pointer] = one_char_option + two_char_option
            pointer += 1
        return ways_to_split[-1]

        