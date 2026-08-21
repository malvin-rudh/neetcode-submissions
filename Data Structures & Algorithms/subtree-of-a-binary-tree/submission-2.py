# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False

        def check(node, subNode):
            if not node and not subNode:
                return True
            elif not node or not subNode:
                return False
            
            left = check(node.left, subNode.left) # assume returns if left branch is subtree or not
            right = check(node.right, subNode.right) # assume returns if right branch is subtree or not

            if node.val == subNode.val and left and right:
                return True
            return False

        result = False

        if check(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

        