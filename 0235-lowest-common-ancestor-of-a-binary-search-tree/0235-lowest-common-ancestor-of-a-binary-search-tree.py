# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root):
            if not root:
                return None
            if root.val > p.val and root.val > q.val:
                return helper(root.left)
            elif root.val < p.val and root.val < q.val:
                return helper(root.right)
            else:
                # If p and q have a differet value, then we found an ansestor for them
                return root
        
        return helper(root)
            
        