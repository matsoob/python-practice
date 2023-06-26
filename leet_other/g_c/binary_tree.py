# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional
from tree.tree import TreeNode, makeTree

class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        total_points = n
        if not root:
            return False
        def find_red_node() -> TreeNode:
            fifo = deque()
            fifo.append(root)
            while fifo:
                current = fifo.popleft()
                if current.val == x:
                    return current
                if current.left:
                    fifo.append(current.left)
                if current.right:
                    fifo.append(current.right)
            raise Exception()
        def count(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            else:
                return 1 + count(node.left) + count(node.right)
        
        red_node = find_red_node()
        left_of_red = count(red_node.left)
        right_of_red = count(red_node.right)
        above_red = total_points - left_of_red - right_of_red - 1
        if max(left_of_red, right_of_red, above_red) > total_points // 2:
            return True
        else:
            return False

sol = Solution()
tree = makeTree([1,2,3,4,5,6,7,8,9,10,11])
print(sol.btreeGameWinningMove(tree, 11, 3))
tree = makeTree([1,2,3])
print(sol.btreeGameWinningMove(tree, 3, 1))