# https://leetcode.com/problems/binary-tree-inorder-traversal/

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ## Recursion
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if not root:
            return result
        if root.left:
            left_branches = self.inorderTraversal(root.left)
            result.extend(left_branches)
        result.append(root.val)
        if root.right:
            right_branches = self.inorderTraversal(root.right)
            result.extend(right_branches)
        return result
    
    ## Non-recursion 1
    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        temp_storage = list()
        if not root:
            return result
        temp_storage.append(root)
        while temp_storage:
            curr = temp_storage.pop()
            if not curr.left:
                result.append(curr.val)
                if curr.right:
                    temp_storage.append(curr.right)
            else:
                temp = curr.left
                curr.left = None 
                temp_storage.append(curr)
                temp_storage.append(temp)   
        return result

    ## Non-Recursion 2
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        temp_storage = list()
        if not root:
            return result
        current = root
        while current or temp_storage:
            if current:
                temp_storage.append(current)
                current = current.left
            else:
                temp = temp_storage.pop()
                # current should not have a left child
                result.append(temp.val)
                current = temp.right
        return result

     
