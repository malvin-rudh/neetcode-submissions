# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
            Note that this is a preorderproblem where you go from the parent to the child
            Also, notice that there's no need to store all the nodes in the path from the root to a particular node, we just need the largest node value in the current path excluding the current node
            If the largest node value is less than the curr node val, then this curr node must be a good node and we should update the curr_largest, else it's not and we move on
            And since this is an additional information that we need to have traversing down the tree(parent --> child), it's useful to use a helper function
            Each recursive call of dfs(node, x) will return the curr largest element in the path excluding the current node
        """  
        good_nodes = 0

        def dfs(node, curr_largest):
            nonlocal good_nodes

            if not node:
                return

            if node.val >= curr_largest:
                good_nodes += 1
            
            new_largest = max(node.val, curr_largest)
            
            dfs(node.left, new_largest)
            dfs(node.right, new_largest)

        dfs(root, float("-inf"))
        return good_nodes