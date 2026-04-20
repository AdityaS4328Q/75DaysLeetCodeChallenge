# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            # If both p and q are greater than parent, LCA must be in right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
                
            # If both p and q are lesser than parent, LCA must be in left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
                
            # We found the split point (or one of the nodes is the current node)
            else:
                return curr