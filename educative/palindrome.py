def is_palindrome(s: str) -> bool:
    if not s:
        return True
    n = len(s)
    left = 0
    right = n - 1

    def rest_is_good(left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if s[left + 1] == s[right]:
                if rest_is_good(left+2, right-1):
                    return True
            if s[left] == s[right - 1]:
                if rest_is_good(left+1, right-2):
                    return True
            return False
    return True

test_cases = [
    ('madame', True),
    ('dead', True),
    ('abca', True),
    ('tebbem', False),
    ('eeccccbebaeeabebccceea', False),
    ('abcdedadedecba', True)
]


if __name__ == '__main__':
    for input, output in test_cases:
        assert is_palindrome(input) == output