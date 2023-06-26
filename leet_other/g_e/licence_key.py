class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        upper = s.replace('-', '').upper()
        n = len(upper)
        licence_builder = list()
        string_builder = list()
        pointer = n - 1
        while pointer >= 0:
            string_builder.append(upper[pointer])
            if len(string_builder) == k:
                string_builder.reverse()
                licence_builder.append(''.join(string_builder))
                string_builder = list()
            pointer -= 1
        if string_builder:
            string_builder.reverse()
            licence_builder.append(''.join(string_builder))
        licence_builder.reverse()
        return '-'.join(licence_builder)


if __name__ == '__main__':
    sol = Solution()
    print(sol.licenseKeyFormatting("5F3Z-2e-9-w", 4)) # "5F3Z-2E9W"
    print(sol.licenseKeyFormatting("2-5g-3-J", 2)) # "2-5G-3J"