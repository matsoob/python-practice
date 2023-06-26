
from typing import List


class Solution:
    def expand(self, s: str) -> List[str]:
        if not s:
            return []
        # {a,b}c{d,e}f -> [[a,b], c, [d,e], f]
        tokenised = list()
        pointer = 0
        is_paren_open = False
        current_paren = list()
        while pointer < len(s):
            if s[pointer] == '{':
                is_paren_open = True
            elif s[pointer] == '}':
                is_paren_open = False
                current_paren.sort()
                tokenised.append(current_paren)
                current_paren = list()
            elif is_paren_open:
                if s[pointer] != ',':
                    current_paren.append(s[pointer])
            else:
                tokenised.append(s[pointer])
            pointer += 1
        n = len(tokenised)
        words = list()
        for i in range(n):
            new_words = list()
            if not words:
                if type(tokenised[i]) == list:
                    new_words.extend(tokenised[i])
                else:
                    new_words.append(tokenised[i])
            else:
                for word in words:
                    if type(tokenised[i]) == list:
                        for char in tokenised[i]:
                            new_words.append(word + char)
                    else:
                        new_words.append(word + tokenised[i])
            words = new_words
        return words


        