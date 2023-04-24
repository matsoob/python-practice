# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List



class Solution:
    combinations = {
        '2': list(['a','b','c']),
        '3': list(['d','e','f']),
        '4': list(['g','h','i']),
        '5': list(['j','k','l']),
        '6': list(['m','n','o']),
        '7': list(['p','q','r', 's']),
        '8': list(['t','u', 'v']),
        '9': list(['w','x', 'y', 'z']),
    }
    def letterCombinations(self, digits: str) -> List[str]:
        combos = list()
        for dig in digits:
            chars = self.combinations.get(dig)
            if not combos:
                for char in chars:
                    combos.append([char])
            else:
                extended = list()
                for current in combos:
                    for char in chars:
                        extended.append([*current, char])
                combos = extended
        combos = [''.join(c) for c in combos]
        return combos