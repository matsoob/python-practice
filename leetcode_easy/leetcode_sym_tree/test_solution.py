import unittest
from solution import Solution, TreeNode


class TestCase(unittest.TestCase):
    def test_solution(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
        sol = Solution()
        self.assertEqual(sol.isSymmetric(root), True)

    def test_solution_one(self):
        root = TreeNode(1)
        sol = Solution()
        self.assertEqual(sol.isSymmetric(root), True)

    def test_solution_two(self):
        root = TreeNode(1, TreeNode(2))
        sol = Solution()
        self.assertEqual(sol.isSymmetric(root), False)
    
    def test_solution_three(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        sol = Solution()
        self.assertEqual(sol.isSymmetric(root), False)

        
    def test_solution_three_true(self):
        root = TreeNode(1, TreeNode(3), TreeNode(3))
        sol = Solution()
        self.assertEqual(sol.isSymmetric(root), True)
if __name__ == '__main__':
    unittest.main()