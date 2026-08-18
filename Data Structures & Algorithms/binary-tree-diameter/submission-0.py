# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def dfs(node):
            nonlocal best
            if not node:
                return 0
            
            left = dfs(node.left) # returns height of left node
            right = dfs(node.right) # returns height of right node
            
            diameter = left + right
            best = max(best, diameter)
            return 1 + max(left, right) # returns the height of the curr node

        dfs(root)
        return best