# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        # Loop until we've processed the required nodes
        while stack or curr:
            # 1. Dive as deep down the left side as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. Process the smallest available node
            curr = stack.pop()
            k -= 1
            
            # 3. If we've hit the k-th node, return its value
            if k == 0:
                return curr.val
            
            # 4. Move to the right subtree and repeat
            curr = curr.right