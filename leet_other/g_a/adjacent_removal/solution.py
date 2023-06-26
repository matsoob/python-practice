
class Solution:
    def removeDuplicatesNaive(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        i = 0
        while i < len(s) - 1 and len(s) > 1:
            if s[i] == s[i+1]:
                s = s[0:i] + s[i+2:]
                i = 0
            else:
                i += 1
        return s
    
    def removeDuplicates(self, s: str) -> str:
        stack = list()
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            elif stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
