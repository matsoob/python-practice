# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:            
                    return i
        return -1
    
    def rabin_karp(self, haystack: str, needle: str) -> int:
        pass
        # lol, maybe I'll try again later
        # if len(haystack) < len(needle): 
        #     return -1

        # target_len = len(needle)
        # haystack_hash = []
        # curr_hash = 
        # for i in range(1, len(haystack) - len(target_len) + 1):
            