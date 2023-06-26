class Solution:
    def lengthLongestPath(self, input: str) -> int:
        def is_file(file_name: str) -> bool:
            return file_name.count('.') > 0
        current_parents = list()
        current_depth = 0
        current_max_file_length = 0
        split = input.split('\n')
        for item in split:
            depth = item.count('\t')
            item = item.replace('\t', '')
            if depth > current_depth:
                if is_file(item):
                    path = '\\'.join([*current_parents, item])
                    current_max_file_length = max(current_max_file_length, len(path))
                else:
                    current_depth += 1
                    current_parents.append(item)
            elif depth == current_depth:
                if is_file(item):
                    path = '\\'.join([*current_parents, item])
                    current_max_file_length = max(current_max_file_length, len(path))
                else:
                    current_depth += 1
                    current_parents.append(item)
            else:
                for _ in range(current_depth - depth):
                    current_depth -= 1
                    current_parents.pop()
                if is_file(item):
                    path = '\\'.join([*current_parents, item])
                    current_max_file_length = max(current_max_file_length, len(path))
                else:
                    current_depth += 1
                    current_parents.append(item)
        return current_max_file_length

# test = '
# dir\n
# \tsubdir1\n
# \t\tfile1.ext\n
# \t\tsubsubdir1\n
# \tsubdir2\n
# \t\tsubsubdir2\n
# \t\t\tfile2.ext'

sol = Solution()
test = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
print(sol.lengthLongestPath(test))