# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from tree.tree import TreeNode, makeTree

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        current_layer = [root]
        current_layer_total = 0

        while current_layer:
            current_layer_total = 0
            next_layer = list()
            for node in current_layer:
                current_layer_total += node.val
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            current_layer = next_layer
        
        return current_layer_total


if __name__ == "__main__":
    sol = Solution()
    root = makeTree([6,7,8,2,7,1,3,9,None,1,4,None,None,None,5])
    print(sol.deepestLeavesSum(root))