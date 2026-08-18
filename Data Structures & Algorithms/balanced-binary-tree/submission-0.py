# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # helper function returns the bool balanced or not, height of left subtree
        # and height of right subtree, i.e. info that the parent node needs to 
        # determine if the tree as per the current node is balanced or not
        def helper(node):
            if not node:
                return [True, 0]
            
            left, height_left = helper(node.left)
            right, height_right = helper(node.right)

            height = 1 + max(height_left, height_right)
            if not left or not right or abs(height_left - height_right) > 1:
                return [False, height]
            
            return [True, height]
    
        ans, height = helper(root)

        return ans
            

