# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. Both nodes are null: they are identical
        if not p and not q:
            return True
        
        # 2. One node is null while the other isn't, OR values don't match
        if not p or not q or p.val != q.val:
            return False
        
        # 3. Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)