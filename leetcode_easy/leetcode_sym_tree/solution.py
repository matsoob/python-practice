# https://leetcode.com/problems/symmetric-tree/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)


    def helper(self, left_node: Optional[TreeNode], right_node: Optional[TreeNode]) -> bool:
        if not left_node and not right_node:
            return True
        if not left_node or not right_node:
            return False
        if left_node.val != right_node.val:
            return False
        if not self.helper(left_node.left, right_node.right):
            return False
        if not self.helper(left_node.right, right_node.left):
            return False
        return True



        

        
