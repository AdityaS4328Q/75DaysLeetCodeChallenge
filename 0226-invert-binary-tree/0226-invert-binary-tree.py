# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. Base case: if the node is empty, there's nothing to invert
        if not root:
            return None
        
        # 2. Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # 3. Recursively invert the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # 4. Return the root of the inverted tree
        return root