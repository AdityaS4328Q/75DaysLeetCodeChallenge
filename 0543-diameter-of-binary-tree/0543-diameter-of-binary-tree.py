# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0  # Global variable to track the max diameter found
        
        def dfs(curr):
            if not curr:
                return 0
            
            # Find the height of left and right subtrees
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            # Update the global result if (left + right) is larger
            # This represents the path passing THROUGH the current node
            self.res = max(self.res, left + right)
            
            # Return the height of this node to its parent
            return 1 + max(left, right)
            
        dfs(root)
        return self.res