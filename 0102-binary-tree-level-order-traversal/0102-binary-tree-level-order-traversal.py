# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        # Initialize a queue and add the root node
        q = collections.deque()
        q.append(root)
        
        while q:
            # How many nodes are currently in the queue?
            # This tells us exactly how many nodes are on the current level.
            level_length = len(q)
            level_vals = []
            
            # Process all nodes on the current level
            for i in range(level_length):
                node = q.popleft()
                level_vals.append(node.val)
                
                # Add children to the queue for the NEXT level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Add the current level's values to our final result
            res.append(level_vals)
            
        return res