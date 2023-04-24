# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional


class Solution:
    def maxDepthRecursive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepthRecursive(root.left), self.maxDepthRecursive(root.right)) + 1

    def maxDepthNotRecursive(self, root: Optional[TreeNode]) -> int:
        layers = 0
        if not root:
            return layers
        temp = list()
        temp.append(root)
        while temp:
            layers += 1
            layer = temp
            temp = []
            while layer:
                curr = layer.pop()
                if curr.left:
                    temp.append(curr.left)
                if curr.right:
                    temp.append(curr.right)
        return layers
        