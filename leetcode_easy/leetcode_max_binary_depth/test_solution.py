from collections import deque
from typing import List, Optional
import unittest
from solution import TreeNode, Solution

test_cases = [
    ([3,9,20,None,None,15,7], 3), 
    ([1,None,2], 2)
]

def makeTree(input: List[int]) -> Optional[TreeNode]:
    if not input:
        return None
    length = len(input)
    def inner(i: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        if i >= length  or input[i] is None:
            return None
        node = TreeNode(input[i])
        node.left = inner(2 * i + 1)
        node.right = inner(2 * i + 2)
        return node
    return inner()

def print_tree(root: TreeNode):
    temp = deque()
    temp.append(root)
    while temp:
        layer = list()
        while temp:
            layer.append(temp.popleft())
        line_to_print = ''
        for node in layer:
            if node:
                line_to_print = line_to_print + ' ' + str(node.val)
                temp.append(node.left)
                temp.append(node.right)
            else:
                line_to_print = line_to_print + ' X'
        print(line_to_print)


class TestCase(unittest.TestCase):
    def test_solution_recursive(self):
        sol = Solution()
        for input, output in test_cases:
            root = makeTree(input)
            self.assertEqual(sol.maxDepthRecursive(root), output)

    def test_solution_non_recursive(self):
        sol = Solution()
        for input, output in test_cases:
            root = makeTree(input)
            self.assertEqual(sol.maxDepthNotRecursive(root), output)


if __name__ == '__main__':
    unittest.main()