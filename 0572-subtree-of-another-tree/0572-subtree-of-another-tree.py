# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 1. If the main root is empty, it can't contain a subRoot
        if not root:
            return False
        
        # 2. Check if the current node's tree matches subRoot
        if self.isSameTree(root, subRoot):
            return True
        
        # 3. If not, check the left and right children recursively
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        # Reusing our logic from Problem 100
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)