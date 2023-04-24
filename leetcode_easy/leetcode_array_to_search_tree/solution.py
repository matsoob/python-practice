# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)
        def makeTree(start: int, end: int) -> Optional[TreeNode]:
            if start == end:
                return TreeNode(nums[start])
            if end < start:
                return None
            midpoint = int((start + end) / 2)
            root = TreeNode(nums[midpoint])
            root.left = makeTree(start, midpoint-1)
            root.right = makeTree(midpoint+1, end)
            return root
        return makeTree(0, length-1)