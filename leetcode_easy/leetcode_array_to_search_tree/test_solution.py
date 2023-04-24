from collections import deque
from typing import List, Optional
import unittest
from solution import Solution, TreeNode

test_cases = [
    ([-10,-3,0,5,9], [0,-10,5,None,-3,None,9])
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

def deconstructTree(root: Optional[TreeNode]) -> List[int]:
    result = list()
    temp = deque()
    if root:
        temp.append(root)
    while temp:
        current_node = temp.popleft()
        if current_node:
            result.append(current_node.val)
        else: 
            result.append(None)
        if current_node:
            temp.append(current_node.left)
            temp.append(current_node.right)
            
    return result

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            print(sol.sortedArrayToBST(input))
            self.assertEqual(deconstructTree(sol.sortedArrayToBST(input)), output)

if __name__ == '__main__':
    unittest.main()
