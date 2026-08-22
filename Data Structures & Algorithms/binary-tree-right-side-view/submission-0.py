# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # you want the nodes, where it is the last processed node in that particular level
        # This problem is a level-order problem, because you don't really need any information from children or ancestor
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            result.append(queue[-1].val)

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

