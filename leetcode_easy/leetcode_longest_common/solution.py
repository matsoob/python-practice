# https://leetcode.com/problems/longest-common-prefix/
from typing import List

class Diverged(Exception):
    pass

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Thought about Tries, but given we aren't counting prefix matches,
        # we end up needing to examine the letters of every word anyway so 
        # there is no way this isn't O(n*m), so I don't see how a Trie would be applicable/helpful
        curr = 0
        if len(strs) == 0:
            return ''
        not_diverged = True
        while not_diverged:
            if len(strs[0]) <= curr:
                break
            for i in range(1, len(strs)):
                if len(strs[i]) <= curr:
                    not_diverged = False
                    break
                if strs[0][curr] != strs[i][curr]:
                    not_diverged = False
                    break
            if not not_diverged:
                break   
            curr +=1

        return strs[0][0:curr]


    def longestCommonPrefixWithException(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        for i in range(0, len(strs[0])):
            try:
                for j in range(1, len(strs)):
                    if len(strs[j]) <= i:
                        raise Diverged
                    if strs[0][i] != strs[j][i]:
                        raise Diverged
            except Diverged:
                return strs[0][0:i]
        return strs[0]
    
    def longestCommonPrefixNoException(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        for i in range(0, len(strs[0])):
            for j in range(1, len(strs)):
                if len(strs[j]) <= i:
                    return strs[0][0:i]
                if strs[0][i] != strs[j][i]:
                    return strs[0][0:i]
        return strs[0]