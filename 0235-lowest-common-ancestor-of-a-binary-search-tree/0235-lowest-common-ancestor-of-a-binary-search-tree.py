# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca=[root]
        def search(root):
            if not root:
                return
            lca[0]=root
            if p.val == root.val and q.val == root.val:
                return
            elif p.val < root.val and q.val < root.val:
                search(root.left)
            elif p.val > root.val and q.val >root.val:
                search(root.right)
            else:
                return

        search(root)
        return lca[0]