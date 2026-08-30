# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
            Intuitively, we can just traverse the BST in-order, this would mean traversing it in a ascending sorted order, which means
            we can just maintain a global index whil traversing the tree, then once this index is equal to k, we can just return the value
            of this node, i.e. the k-th smallest value in the tree
        """

        index = 0

        def inorder(node):
            nonlocal index

            if not node: 
                return None
            
            left_result = inorder(node.left)
            
            if left_result is not None:
                return left_result

            index += 1

            if index == k:
                return node.val
            
            return inorder(node.right)

        return inorder(root)