import unittest
from solution import Solution, TreeNode

test_cases = [

]

class TestCase(unittest.TestCase):
    def test_solution(self):
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        sol = Solution()
        result = sol.inorderTraversal(root)
        self.assertEqual(result, [1,3,2])

    def test_solution_single(self):
        root = TreeNode(1)
        sol = Solution()
        result = sol.inorderTraversal(root)
        self.assertEqual(result, [1])

    def test_solution_empty(self):
        sol = Solution()
        result = sol.inorderTraversal(None)
        self.assertEqual(result, [])
if __name__ == '__main__':
    unittest.main()
